# slu #
The last Songlib utility you'll ever need (name subject to change).

NOTE: currently, this readme references functionality yet to be implemented; think of it as a way for me to plan functionality and get feedback on my planning. This will also make it easier for me to compile the man page later. If I goof on how something should be written in a man page, please let me know.



## Name ##
	slu -- SongLib Utility 

## Synopsis ##

'git clone https://github.com/lusth-music/slu.git' to retrieve repository
'make' && 'make install' to install slu (will need developer tools)

'slu [convert file_name target_type] [install [-p optional_path]] [help] [mix [file1, file2, ...]] [new [-p optional_path, file1, file2, ...]] [play [file]] [remove] [repair] [update [sl][slu]] [version]'

## Description ##
'slu' is a utility program designed to make installing, updating, and writing music with Songlib, a C music library, easier. Songlib and its documentation is available [here](http://www.songlib.cs.ua.edu).

For security purposes, 'slu' cannot be run as the superuser. If administrative permissions are required by an operation, you will be prompted by sudo for the necessary password.

'slu' accepts the following commands:

convert file_name target_type			Convert an RRA file to another format, or vice versa. Without 'sox' installed, only RRA->WAV/WAV->RRA is possible. 'slu' will determine 										the best conversion path from the source and target filetypes.

										Target types include rra, wav, mp3, and others. Run 'sox' without options to see the available audio types.

install [-p optional_path noDeps]		Installs the latest available version of Songlib and any dependencies/corequisuites. By default, 'slu' will install the songlib files to 
										~/.songlib; the -p flag allows you to specify a different location. 

										By default, 'slu' will attempt to detect your environment/package manager, and will try to run the necessary commands for dependency/corequisite installation (you may be prompted for a root/sudo password). Currently, 'slu' supports 'apt-get' (Debian) and Homebrew (OS X). If 'slu' does not yet support your package manager, you can use noDeps to block 'slu' from installing dependencies.

help									Shows the usage information.

mix [file1, file2, ...]					Passthrough to 'rrafastmixer'/'rraplay' (will mix files, then play them). The files should be in RRA format.

new name [-p optional_path, file1, file2, ...]	Create a new songlib project. By default, slu will create it in ~/songlib/projects/[name]. You can specify a path for the 												project to be created in, as well as the filenames for your instrument files.

play [file]								Passthrough to 'rraplay'. File should be in RRA format.

remove									Uninstall songlib. This will not remove any dependencies/corequisites (to prevent issues if other applications use them).

repair									Repair the current songlib installation. Use this if you are having issues with the library.

update [sl][slu]						Update Songlib and 'slu'. By default, both will be checked for updates. You can specify 'sl' or 'slu' to only update one.

version									Prints version information for slu and songlib (if installed).

## See Also ##

songlib(3)

## Authors ##

TODO