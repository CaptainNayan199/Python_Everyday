# Playing with python
# So today we are going to see about some functions in file handling like tell(), seek(), etc.

# Doing miscellaneous things in python

# seek() & tell() functions in python - this methods are used in python to play with various objects and theirs position within the file. They are built in functions, which makes file reading and writing bit easier and consistent.

# seek() -  this functions allows us to move the current position within a file to a specific point, the position is specified in bytes. We can move either forward or backward fro the current position


with open("file.txt", 'r') as file:
    f.seek(5) #this will move to the 10th byte location in the file; 123456789 - contents of the file, then it will move to 6(after 4 byte)
    data = f.read() #read from the 6





