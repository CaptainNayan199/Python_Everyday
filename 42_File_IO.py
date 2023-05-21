# So today we are going to see about file input and output in python
# We can interfere with files using python in various mode like read, write,  and other as well.
# Different file handling methods are used to interfere with files in python.
# This methods are built-in  in python

# Here i have created a new file with name file_handling.txt, wo we will perform action on this file.

# Different file handling methods in python

# read()-r -  this mode is used in opening a certain file in reading mode. If user forgot to mention which mode he/she wanna open the file then the file is opened in reading mode. It is the default one. If python does not finds the mentioned, file than it returns errros saying file not found.

# write()-w - this mode is used in opening a certain file in writing mode. If mentioned file is not found then the python creates a new file in thie mode, without throwing an error.

# append()-a - this mode is used in opening a file in appending mode. Append means to add something in a particular things. As like write mode, this mode also creates a new file if the mentioned file is not found without throwing an error.

# create()-x - this method is used in creating a new file, will throws an error if file already exists.


# File handling modes in python

# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the new file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.


# Opening a file - for opening a file in python we need to use open() method that takes two arguments; name of the file and the mode in which we are going to open that particular file

open_file = open("file_handling.txt", 'r') # so basically this commmand will open a particular file in reading mode.

# but yet we havent displayed the content of the file.
# So to display the content of the file


data = open_file.read() # so this line of code will read all the contents inside of the file, abstracting the contents of the file.
print(data) # displaying the contents. 
open_file.close() # closing the file.


# Writing a file - we use write methods to write some contents inside of a file

fopen = open("write.txt" , "w")
fopen.write("This is a new txt file for writing methods")
fopen.close()

# PS : Closing a file always can seem quite hectic! What if i say we can use a certain function which lets us not to close the file manually, the python automatically does it 

with open("write.txt","w") as file: # this with keyword is use to automatically close the file
    file.write("This is a new text file for writing methods")
    file.write("This is writing a file with the use of `with` keyword ")

# Appending a file - this method is used to insert or append something into the file

with open("file3.txt", "a") as file:
    file.write("This is appending something into the file with a methods \n")
    data_inside_file = file.read()
    print(data_inside_file)

# Now what if we want to append as well read the contents of the file at the same time ? We can use a+ method for it and read the contents of the file as well.


# with open("file3.txt", "a+") as file:
  #  file.write("This is reading a file with a+ methods \n")
   # data_inside_file = file.read()
    #print(data_inside_file)



 
 
