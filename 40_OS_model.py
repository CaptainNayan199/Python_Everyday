# So today we are going to see about OS module in python
# This module is ued to interfere with OS of the computer and perform task accordingly
# Its a built in module in python 

# PS : There are hundreds and hundreds of different methods inside OS  module in python and i cannot talk about all in single session

# So i am just trying to say what this module actually does

# The functions OS module provides allows us to operate on underlying Operating System tasks, irrespective of it being a Windows Platform, Macintosh or Linux.  - this is the main work done by OS module

# Suppose i want to create a new folder , how can i do that?

import os

os.mkdir("New test folder") # - this command will create a new folder

# we can even create a multiple foder, by simply using for loop


for i in range(1,100):
    os.mkdir(f"New folder {i} ") # now this command will create 100 folder

# changing directory 

os.chdir("/nayan") # this command can be used to change the working directory

# deleting a directory 

os.rmdir("dir_name")

# renaming a directory

os.rename("original_name", "final_name")

# openinga file 

os.open(" ")

# So there are many and many different methods and functions inside this module
# You can have a look at those by following the below provided link, if only you are interested
print("https://docs.python.org/3/library/os.html")

# So yeah i did not planned to make this session too long as al the things have been clearly mentioned in the docs. Try visiting and reading the docs for better understanding of the python 