# So today we are going to see about file input and output in python
# We can interfere with files using python in various mode like read, write,  and other as well.
# Different file handling methods are used to interfere with files in python.
# This methods are built-in  in python

# Here i have created a new file with name file_handling.txt, wo we will perform action on this file.

# Different file opening modes in python

#Opening a file - for opening a file in python we need to use open() method that takes two arguments; name of the file and the mode in which we are going to open that particular file

open_file = open("file_handling", 'r') # so basically this commmand will open a particular file in reading mode.

#  but yet we havent displayed the content of the file.
# So to display the content of the file


data = open_file.read() # so this line of code will read all the contents inside of the file, abstracting the contents of the file.
print(data) # displaying the contents.
open_file.close() # closing the file.

 
 
