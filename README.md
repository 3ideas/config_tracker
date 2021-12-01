
# config_tracker
> This is a utiltiy to help track configuration changes in database tables and files. It can track changes in one system or accross many systems. It is currently aimed at a certain ADMS, but can easily be adapted for other uses.


This is designed for system managers/maintainers to see a history of changes made to a systems configuration. It provides reports that enable you to see where changes have been made, when the changes were done and what the changes were. It can also compare tracked items between systems. 

The scripts are all currently been designed to run on linux systems, the reports are output as web pages.

The system to track config changes comes in three parts

- A script to gather the tracked items on a daily bases. (or any other time period).
- A repository to hold the tracked items
- A set of reports that can be run against the repository to see the changes that have been made.

It also has a set of scripts aimed at a specific user, for transfering over from their existing tracking system. These may be useful to anyone doing something similar. 


## Install

Copy the `scripts` directory from this repository to your system ensure they are in your path. 

Note: on the systems that configuration is to be captured only the `track_config.py` script is required.
    
On the system which holds the master repository, all the contents of the `scripts` directory is required. The dependencies of diff2html is also required. Note a local docker build of this is available in the diff2html directory here. You should verify this works on your system first before generating any reports. The daff dependency is included in the scripts directory as daff.py, this has been prebuilt from source. More recent versions may be available in their respective homes below.


## How to use

Decide which system will hold the 'master' copy of the repository, this should be the system where reports are run against as only this system needs to hold all the data from any systems they are gathering information from.

Initialise the repostitory on this system, this can be done as follows where config_repository is the name of the directory that holds the repository. Its name can be anything, but in the examples here it is called `config_repository`
```
mkdir /path_to_repository/config_repository
./initalise_repository.py -s hostname_of_master -r /path_to_repository/config_repository -i

```

This creates a mostly empty git repository in the directory specified. It will have one file in it called `README.md`,
the contents of will be something like
```
This is the repository for all configuration. There should be a git branch for every server recorded here, the local server should be the active branch
```


### On systems being tracked

This git repository created above should now be cloned to every system where configuration tracking should be done.


```
cd /users/bt
git clone username@hostname:/path_to_repository/config_repository/.git
```
Two files need to be created, one with a list of tables to be captured and one with a list of files the are to be tracked in it. In the `examples` directory there is some examples of these files.

A local branch is then created to hold the configuration. This is done with the `-i` option, note the branch name can be specified (`-b  servername`) but it defaults to the hostname of the system we are currently on.
```
track_config.py -F ../examples/file_list.txt -T ../examples/table_names.txt -r /path_to_repository/config_repository -i
```
This will initalise the branch and do an inital capture of the configuration in the repository.

Then push the branch to the master with
```
cd /path_to_repository/config_repository && git push -u origin `hostname`
```

It is suggested that a cron job to run on a regular interval (say every day), to capture configuration. The command to capture configuration and push it to master would be:
```
./track_config.py -F ../examples/file_list.txt -T ../examples/table_names.txt -r /path_to_repository/config_repository
cd /path_to_repository/config_repository && git push origin
```

**NOTE: on the master do not checkout any of the branches being pushed to it. This will result in git failing to push the branches to the master!!**

### Running a report.

The script to generate a report is 
```
generate_report.py -r /path_to_repository/config_repository -a hostname1 -b hostname2 -s path_to_styles/styles -o /path_to_output
```

where `hostname1` and `hostname2` are the names of the servers/branches to compare. The `path_to_styles/styles` should point to the `scripts/styles` directory. If only `-a` is specified it will generate only a history report of that server and not a comparison. If both are given then both history of changes and a comparison between systems is generated.


In the output dir this will generate something like
```
index_server1_server2.html  original_files              server1                     server1_change_history.html server1_server2             server2                     server2_change_history.html styles
```
The entry points into the reports are:
- `index_server1_server2.html` shows the differences between servers.
- `server1_change_history.html` shows the change history of server1
- `server2_change_history.html` shows the change history of server2


## Dependencies

The system requires python >= 2.6 and git.

It also requires utilies to generate diff reports in html format. Currently it uses 

- [diff2html](https://github.com/rtfpessoa/diff2html)
- [daff](https://github.com/paulfitz/daff)

See the development system for notes on how to build these.

## Support

Need help? Please [open an issue](https://github.com/3ideas/config_tracker/issues/new) for support.


## Development and Contributions

See [development guide](BUILD.md)


## License

Copyright 2021-present Bill Traill 3ideas.co.uk. Released under the terms of the MIT license.

If you're using the library in a commercial enviroment or product, please consider sponsoring its development or paying for maintenace of it. Contact bill@3ideas.co.uk 

