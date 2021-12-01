#!/usr/bin/env python2.7
# C--------------------------------------------------------------------------
# C  Program : config_tracker.py
# C
# C  Extracts config data
# C
# C  3ideas.co.uk  18/11/21 BT   Initial Version
# C--------------------------------------------------------------------------
from __future__ import print_function
import csv
import sys
import os
import socket
import argparse
import shutil
import glob
import datetime
from subprocess import call

try:
    from libs.database import RDBMS, Row, NoDataFoundWarning
    db_ok = True
except ImportError:
    db_ok = False

verbose = False

try:
    basestring

    def isstr(s):
        return isinstance(s, basestring)
except:
    def isstr(s):
        return isinstance(s, str)


def run_subprocess(command):
    """
    Run the subprocess
    """
    try:

        retcode = call(command, shell=True)
        if verbose:
            print('Command: %s returned %s' % (command, retcode))
        if retcode < 0:
            if verbose:
                sys.stderr.write('Command %s terminated by signal %s\n' %
                                 (command, -retcode))
        elif retcode > 0:
            if verbose:
                sys.stderr.write('Command %s returned %s\n' %
                                 (command, retcode))
    except OSError as e:
        sys.stderr.write("Execution failed: %s\n" % e)
    return retcode


def mkdir_for_fullpath(filename_output_location):

    path, file = os.path.split(filename_output_location)

    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except OSError as error:
            sys.stderr.write("Directory '%s' cannot be created, skipping file: %s\n" %
                             (error, path))
            return False
    return True


class GitRepositoryUpdater:

    def __init__(self, repository, output_dir=None, branch=None):
        self.repository = repository
        self.branch = branch
        self.output_dir = output_dir

    def run_git_command(self, command):
        """
        Run a git command
        """
        result = run_subprocess('cd %s && git %s' % (self.repository, command))
        return result

    def set_branch(self, branch):
        self.branch = branch

    def commit_repository(self, comment):
        """
        Commit the repository
        """
        result = self.run_git_command('add . ')
        if result != 0:
            print('commit_repository: Failed to add files')
            return result
        result = self.run_git_command('commit -m "%s"' % (comment))
        return result

    def branch_exists(self, branch):
        """
        Check if the branch exists
        """
        result = self.run_git_command(
            'rev-parse --verify %s --quiet >/dev/null 2>/dev/null' % (branch))
        if result != 0:
            return False
        return True

    def create_branch(self, branch):
        """
        Create the branch
        """
        if self.checkout_branch('master') != 0:
            print('create_branch: Failed to switch to master branch')
            return 1

        result = self.run_git_command('branch %s' % (branch))
        if result != 0:
            print('create_branch: Failed to create branch:%s' % branch)
            return result
        if self.checkout_branch(branch) != 0:
            print(
                'create_branch: Failed to switch to branch after creating it: %s' % branch)
            return 1
        filename = os.path.join(self.repository, '%s.md' % branch)
        result = run_subprocess(
            "echo 'This is the branch for: %s, we should only see this file in this branch!' >%s" % (branch, filename))

        # create_base_directories(directory)
        # add_all_new_files_to_respository(directory)
        self.commit_repository(
            "create_branch: Initial commit, of branch: %s" % branch)
        return result

    def checkout_branch(self, branch):
        result = self.run_git_command('rev-parse --abbrev-ref HEAD')
        if result != branch:
            result = self.run_git_command('checkout %s' % (branch))
        return result

    def repository_exists(self):
        """
        Check if the repository exists
        """
        # check if .git and is a directory
        git = os.path.join(self.repository, '.git')
        if os.path.isdir(git):
            return True
        return False

    def branch_is_dirty(self):
        """
        Check if the branch is dirty
        """
        result = self.run_git_command('status --porcelain')
        if result != 0:
            return True
        return False

    def clear_directory(self, directory):
        """remove all files in `directory`"""
        if os.path.isdir(directory):
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)

                if os.path.isdir(file_path):
                    if verbose:
                        print('Deleting directory: %s' % file_path)
                    shutil.rmtree(file_path)
                else:
                    if verbose:
                        print('Deleting file: %s' % file_path)
                    os.remove(file_path)

    def empty_repository(self):
        """
        Empty the repository
        """
        try:
            self.clear_directory(os.path.join(self.repository, 'database'))
            self.clear_directory(os.path.join(self.repository, 'files'))
            return 0
        except Exception as e:
            sys.stderr.write(
                'empty_repository: Failed to empty repository: %s\n' % e)
            return 1

    def mark_last_update(self, branch, table_names, file_names):
        """ Update file with date of last update, this ensures we know updates were done. 
        It also has a list of all the tables and files updated.
        """

        date_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        update_details = 'Last updated for: %s at %s \n' % (branch, date_str)
        update_details += 'Table names:\n'
        for t in table_names:
            update_details += '%s\n' % t
        update_details += '\nFile names:\n'
        for f in file_names:
            update_details += '%s\n' % f

        filename = os.path.join(self.repository, 'last_updated.md')
        hs = open(filename, 'w')
        if hs:
            hs.write(update_details)
            hs.close()
        else:
            sys.stderr.write('Failed to open %s\n' % filename)
        return


def create_base_directories(directory):
    files = os.path.join(directory, 'files')
    database = os.path.join(directory, 'database')
    if not os.path.isdir(files):
        os.mkdir(files)
    if not os.path.isdir(database):
        os.mkdir(database)


def getTableColumns(table_name):
    """ Get all the column names for a given table"""
    rows, columns = RDBMS.fetch_all(
        "select COLUMN_NAME from all_tab_columns where table_name = '%s' order by COLUMN_ID " % table_name)
    column_names = [c[0] for c in rows]
    return column_names


def get_table(table_name):
    """ get all the rows in the table_name, returns them with the column names, the order of the rows returned is sorted by order of the column names """

    columns = getTableColumns(table_name)
    if len(columns) == 0:
        sys.stderr.write('Table name: %s has not been found, skipping\n' %
                         table_name)
        return None, None

    columns_str = ''
    sep = ''
    for column_name in columns:
        columns_str += sep + column_name
        sep = ','

    query = 'select %s\nfrom %s\norder by %s' % (
        columns_str, table_name, columns_str)
    #print('%s \n\n'% query)
    rows, columns = RDBMS.fetch_all(query)
    return rows, columns


def write_table_as_csv(table_name, filename, sep=None, encoding='latin-1', quotechar='"', quoting='nonnumeric'):
    """ Reads the table_name and writes it as a csv file"""
    if sep is None:
        sep = ','

    table_rows, table_column_names = get_table(table_name)
    if table_rows is None:
        return

    if quoting == 'nonnumeric':
        quoting = csv.QUOTE_NONNUMERIC
    elif quoting == 'none':
        quoting = csv.QUOTE_NONE
    elif quoting == 'minimal':
        quoting = csv.QUOTE_MINIMAL
    elif quoting == 'all':
        quoting = csv.QUOTE_ALL
    else:
        sys.stderr.write('Unrecognised quoting option: %s, defaulting to nonnumeric\n' %
                         quoting)
        quoting = csv.QUOTE_NONNUMERIC

    with open(filename, 'w') as csvFile:
        writer = csv.writer(csvFile, quoting=quoting, delimiter=sep,
                            lineterminator='\n', escapechar='\\', quotechar=quotechar)
        writer.writerow(table_column_names)
        for row in table_rows:
            escaped_row = []
            for f in row:
                if isstr(f):
                    try:
                        f = f.replace('\n', '\\n')
                    except Exception as e:
                        sys.stderr.write('In table: %s, error: %s \n%s\n' %
                                         (table_name, e, row))
                escaped_row.append(f)
            writer.writerow(escaped_row)


def read_list_from_file(filename):
    """ Reads a file with table/file names in it and returns a list of the names """
    names = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line != '':
                names.append(line)
    return names


def capture_tables_as_csv(table_names, dest_dir, encoding='latin-1', sep=',', quotechar='"', quoting='nonnumeric'):

    for table_name in table_names:
        write_table_as_csv(table_name, os.path.join(dest_dir, table_name+'.csv'),
                           encoding=encoding, sep=sep, quotechar=quotechar, quoting=quoting)


def capture_file_list_fullpath(file_names, dest_dir):
    """ copies the files in the list to the `dest_dir`, returns a list of the files copied successfully"""

    file_list = []
    for filename in file_names:
        name_list = glob.glob(filename)  # incase we have wild cards !
        for f in name_list:
            if copyfile_fullpath(f, dest_dir):
                file_list.append(f)
    return file_list


def copyfile_fullpath(file_name, dest_dir):
    """ Copy the file to the destination dir in the same directory structure as its original path
    Returns True if file copied OK, False if not"""

    directory_name = os.path.dirname(file_name)
    base_name = os.path.basename(file_name)

    if len(directory_name) > 0 and directory_name[0] == '/':
        directory_name = directory_name[1:]

    dir_to_create = os.path.join(dest_dir, directory_name)

    copy_name = file_name
    if copy_name[0] == '/':
        copy_name = copy_name[1:]

    dest_full_name = os.path.join(dest_dir, copy_name)

    if not os.path.isdir(dir_to_create):
        try:
            os.makedirs(dir_to_create)
        except OSError as error:
            sys.stderr.write("Directory '%s' cannot be created, skipping file: %s\n" %
                             (error, file_name))
            return False
    try:
        shutil.copyfile(file_name, dest_full_name)
    except Exception as e:
        sys.stderr.write("File cannot be copied to dest : %s, skipping file: %s\n" %
                         (e, file_name))
        return False
    return True


if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--table', required=False,
                    help='table name of table to be exported ', default='')
    ap.add_argument('-T', '--tables_filename', required=False,
                    help='File containuing the list of table names to export as csv', default='')
    ap.add_argument('-F', '--files_filename', required=False,
                    help='File containuing the list of files to be copied to destination (full path)', default='')
    ap.add_argument('-f', '--file_copypath', required=False,
                    help='file to be copied to destination (full path is copied)', default='')
    ap.add_argument('-d', '--dest_dir', required=False,
                    help='Directory the files to be stored in', default='./')
    ap.add_argument('-r', '--repository', required=False,
                    help='Repository  the files to be stored in (this overrides the --dest_dir option', default='./')
    ap.add_argument('-b', '--branch', required=False,
                    help='Branch to use, this defaults to the hostname of the system being run on! ', default='')
    ap.add_argument('-i', '--initalise', required=False,
                    help='will create branch ', default=False, action='store_true')
    ap.add_argument('-V', '--verbose', required=False,
                    help='add very chatty output, mainly for debug', default=False, action='store_true')

    ap.add_argument('-e', '--encoding', required=False,
                    help='Character encoding, defaulting to latin-1', default='latin-1')
    ap.add_argument('-s', '--sep', required=False,
                    help='Seperator for csv output, default is ,', default=',')
    ap.add_argument('-q', '--quotechar', required=False,
                    help='Quotation charater for csv output, default is "', default='"')
    ap.add_argument('-u', '--quoting', required=False, help='What type of quoting to use, options are: none, minimal, nonnumeric,all. default is nonnumeric"', default='nonnumeric',
                    choices=['none', 'minimal', 'nonnumeric', 'all'])

    args = vars(ap.parse_args())

    table = args['table']
    tables_filename = args['tables_filename']
    file_copypath = args['file_copypath']
    files_filename = args['files_filename']
    dest_dir = args['dest_dir']
    encoding = args['encoding']
    sep = args['sep']
    quotechar = args['quotechar']
    quoting = args['quoting']
    repository = args['repository']
    verbose = args['verbose']

    table_names = []
    if tables_filename != '':
        table_names += read_list_from_file(tables_filename)
    if table != '':
        table_names.append(table)
    if not db_ok and len(table_names) > 0:
        sys.stderr.write("No database connection, cannot export tables\n")
        sys.exit(1)

    file_names = []
    if files_filename != '':
        file_names += read_list_from_file(files_filename)
    if file_copypath != '':
        file_names.append(file_copypath)

    # If repository given, check it exists and the branch or hostname exists in the repository!
    if repository != '':
        r = GitRepositoryUpdater(repository)

        if not r.repository_exists():
            sys.stderr.write("Repository %s does not exist, exiting!\n" %
                             repository)
            sys.exit(1)

        if args['branch'] == '':
            branch = socket.gethostname()
        else:
            branch = args['branch']

        if not r.branch_exists(branch) and args['initalise']:
            if r.create_branch(branch) != 0:
                sys.stderr.write("Branch %s cannot be created, exiting!\n" %
                                 branch)
                sys.exit(1)

        if not r.branch_exists(branch):
            sys.stderr.write("Branch %s does not exist in repository %s, create with -i ? exiting!\n" %
                             (branch, repository))
            sys.exit(1)

        # verify the branch is currently checked out
        if r.checkout_branch(branch) != 0:
            sys.stderr.write("Branch %s cannot be checked out, exiting!\n" %
                             branch)
            sys.exit(1)

        # check the branch is clean
        if r.branch_is_dirty():
            sys.stderr.write("Branch %s is dirty, please commit changes before running this script!\n" %
                             branch)
            sys.exit(1)

        # empty the files in the repository
        if r.empty_repository() != 0:
            sys.stderr.write("Repository %s cannot be emptied, exiting!\n" %
                             repository)
            sys.exit(1)

        # copy over the files
        capture_tables_as_csv(table_names,
                              dest_dir=os.path.join(r.repository, 'database'),
                              encoding=encoding,
                              sep=sep,
                              quotechar=quotechar,
                              quoting=quoting)
        files_list_copied = capture_file_list_fullpath(file_names,
                                                       dest_dir=os.path.join(r.repository, 'files'))
        # commit the changes
        date_str = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
        r.mark_last_update(branch, table_names, files_list_copied)
        r.commit_repository(date_str)

    else:
        if not os.path.isdir(dest_dir):
            sys.stderr.write("Destination directory %s does not exist, exiting!\n" %
                             dest_dir)
            sys.exit(1)

        capture_tables_as_csv(table_names, dest_dir, encoding=encoding,
                              sep=sep, quotechar=quotechar, quoting=quoting)
        capture_file_list_fullpath(file_names, dest_dir)
