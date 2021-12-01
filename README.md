
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

Copy the scripts to system (usr/local/bin ?) and ensure they are in your path. 




## How to use

Add the scipts someplace in you path.

Decide which system will hold the 'master' copy of the repository, this should be the system where reports are run against as only this system needs to hold all the data from any systems they are gathering information from.

Initialise the repostitory on this system, this can be done 

Identify the location of where the repository should be held.



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

