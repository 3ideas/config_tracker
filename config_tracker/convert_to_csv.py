# AUTOGENERATED! DO NOT EDIT! File to edit: 01_convert_to_csv.ipynb (unless otherwise specified).

__all__ = ['read_headers', 'read__write_from_sep_sv']

# Cell
#! python
import csv
import sys

#C--------------------------------------------------------------------------
#C  Program : covert_to_csv.py
#C
#C  Converts a legacy format style file to csv.
#C  Here for reference only - not part of the working solution
#C
#C  Copyright: 3ideas.co.uk
#C
#C  See https://github.com/3ideas/config_tracker
#C--------------------------------------------------------------------------


def read_headers(header_file):
    """Reads the header file which consists of lines starting with the table name followed by a : and the header.
    It returns a dictionary of table names and their associated header lines.
    """
    header_lines = {}
    with open(header_file, 'r') as f:
        for line in f:
            table_name, header = parse_header_line(line.rstrip("\n"))
            if table_name is not None:
                header_lines[table_name] = header



    return header_lines


def read__write_from_sep_sv(filename,out_filename,in_sep=None,out_sep = None,encoding=None,chop_end_field=True):
    """Reads in a sep file and outputs in proper csv"""
    if in_sep is None:
        in_sep = '|'
    if out_sep is None:
        out_sep = ','

    # TODO: see if we can fix or handle encoding errors? Hack is to set to latin-1
    if encoding is None:
        encoding="latin-1"
    line_number = 0

    fp = open(filename, "r", encoding=encoding)

    row_list =[]
    with open(filename, 'r', encoding=encoding) as fp:
        for line in fp:
            line_number += 1
            line = line.strip()

            fields = line.split(in_sep)  # TODO: use csv reader ?
            if chop_end_field:
                fields.pop()
            if line_number == 1:
                number_of_fields = len(fields)
            else:
                if len(fields) != number_of_fields:
                    print(f"{filename}  inconsistent number of fields on line: {line_number}",file=sys.stderr)
            row_list.append(fields)

    with open(out_filename,'w',encoding=encoding) as fo:
        writer = csv.writer(fo,quoting=csv.QUOTE_MINIMAL,delimiter=out_sep)
        writer.writerows(row_list)



# Cell
try: from nbdev.imports import IN_NOTEBOOK
except: IN_NOTEBOOK=False

if __name__ == "__main__" and not IN_NOTEBOOK:
    import argparse
    import os
    import sys

    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True,
                help="file to be converted")
    ap.add_argument("-o", "--output", required=False,default='',
                help="output filename")
    ap.add_argument("-e", "--encoding", required=False,default=None,
                help="file encoding, defaults to latin-1")
    args = vars(ap.parse_args())

    filename = args["file"]
    output_filename = args['output']
    encoding = args['encoding']

    # Stip the suffex of the filename to get the table_name
    base=os.path.basename(filename)
    table_name = os.path.splitext(base)[0]

    if output_filename == '':
        output_filename = table_name + '.csv'
    read__write_from_sep_sv(filename,output_filename,encoding)