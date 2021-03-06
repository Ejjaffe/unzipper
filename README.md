# Unzipper.py

## Description

Unzips *all* zip files in the folder you run it from. 

Unzipping a large number of zip files can be quite a laborious task to do manually and "select all/extract here" only extracts the first selected file in windows 10. That's why this utility exists.

It should just work right out of the box if you already have python, no frills or complicated stuff.

**Beware:** When it unzips, it will overwrite existing directories with the same names as the zip files. **You can avoid disaster by renaming any files or folders with matching names.** For example, if there's a "my_zip_file.zip" and a "my_zip_file" folder, rename one of them to avoid losing the folder. If you can't do that, don't use the tool. Could I have added a catch for that? Sure. But I didn't need that when I made it.

## Requirements:
OS: should work on nearly all Windows, linux, and possibly some Mac OS's.

Python: Version 2.7 or higher, (still works on 3.8).

## To use: 

### Basic Computer Users:

1) Install python 2.7 (or higher) if you don't have it.

2) Create a text file in the folder containing the zip files. (Windows: Right click > New > text file)

3) Copy-paste the contents of unzipper.py into this text file 

4) Save it as "unzipper.py". (Windows: ctrl+shift+s should open the save-as window.)

5) Double click unzipper.py in the folder to run it.

### If you know how to use git/ know your way around a computer:

0) Install python 2.7 (or higher) if you don't have it.

1) git clone this repo anywhere.

2) Copy-paste unzipper.py into the directory with zip files.

3) Run unzipper.py in an IDE, via CMD (cd copy/paste/dir/with/zips/here; python unzipper.py), or by double-clicking it.

## Notes
Unzipper.py is designed to work for python versions 2.7 (most common for old systems) to 3.8 (the most recent one). It only imports standard packages, so there's no need to `pip install` anything.

You can find out which python version you have installed by default by opening your command prompt (menu > search "CMD") and typing `python --version`. If it says *"'python' is not a recognized command"*, you probably don't have python installed. If that's not the case, try using `python2.7` or specify whatever version you have installed.

To install python, you can use the links below and follow the instructions. If it's your first time installing a program or you feel uncomfortable,  ask for help.

https://www.python.org/downloads/

https://realpython.com/installing-python/

# Unzipper.bash -- linux

No need to download, cd to your directory of choice and run `unzip *.zip` or `unzip \*.zip`. Or just copy to your directory of choice and run, but that seems like more work.
