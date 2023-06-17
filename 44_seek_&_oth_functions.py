# Playing with python
# So today we are going to see about some functions in file handling like tell(), seek(), etc.

# Doing miscellaneous things in python

# seek() & tell() functions in python - this methods are used in python to play with various objects and theirs position within the file. They are built in functions, which makes file reading and writing bit easier and consistent.

# seek() -  this functions allows us to move the current position within a file to a specific point, the position is specified in bytes. We can move either forward or backward fro the current position


with open("file.txt", 'r') as file:
    file.seek(5) #this will move to the 10th byte location in the file; 123456789 - contents of the file, then it will move to 6(after 4 byte)
    data = file.read() #read from the 6


# tell() - this built in function in python returns the current position within the file in bytes. It can be useful to keep track of the current location of the file

with open("file.txt", 'r') as file:
    f = file.read(10) # reading upto 10 bytes
    current_loc = file.tell() # determining the current position of the file
    f.seek(current-loc) #seeking to the saved location


# truncate() -  this function is used to truncate the file to a specific size (in byte)

with open("file.txt", 'w') as file:
    f.write("Nayan Pathak") # writing Nayan pathak into the file
    f.truncate(3) # Specifying to only keep the first 3 bytes in the file, truncate all others.

# Now if we try opening the content of the file then : 
with open("file.txt", 'r') as file:
    print(file.read()) # Gives Nay, as we have truncate all others.
