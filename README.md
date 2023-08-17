# cladoup_files
A program for automatically copying files at a specified interval. Allows you to specify a specific target file or an entire folder as a copy source, which is copied while preserving the internal structure.

The program takes as arguments: the path to the folder\files to copy "source_path", the path to the folder to save "destination_path", the copying interval in seconds "interval" and the maximum number of simultaneously stored copies "max_copies".
When the number of copies made reaches the value specified in "max_copies", the program starts deleting the oldest copy each time a copy is made. Copies are added to the specified path with the creation inside a folder named as the current timestamp.

Works in two modes:
1. Parameters for copying can be registered in the console window. Paths entered manually in the console window are separated by '\\\'.
2. Can be loaded from config.json. The paths specified in config.json must be separated by '\\\\'. If "silence_mode": true in config.json, then the program runs in the background and the start of the copy process does not require additional confirmation from the user after starting the program, and all output occurs in log.txt.

If you run several parallel processes of copying different files, then it is better to specify folders with different names along the save path, in order to avoid errors associated with creating folders with the same names inside the current timestamp.

"language": "en" - English (Google Translate)
"language": "ru" - Russian language.

*To work on Windows 7, you may need to install security update KB3063858. For the 32-bit version, the offline installer is in the archive.
