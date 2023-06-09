# So today we are going to see some important file methods in python like read(), readlines(), writelines() etc.

# readlines() methods - this methods is used to read a single line from the file line by line, multiple lines can also be read by the use of loop 

f = open("myfile.txt", 'r') #opening a file in read mode
while True: #using while loop
    line = f.readline() #using the readline method
    if not line: # if not is a special keyword in which checks whether the resepected line is there in the file or not and returns true if not found, else return false
        break #if not found this loop will break 
    print(line) #print the line


# writelines() - this method is used to write a sequence of strings to a file. we can write any iterable objects like list or tuples by the use of this methods.



f = open("myfile1.txt", 'w') #creating and opening a new file.
data = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n', 'This is line 4'] # some data, 4 lines of data
f.writelines(data) #writing 4 lines of data with the use of writelines() methods,
f.close() #closing the file

# PS: This methods does not adds new line (\n) automatically in between the data , we have to manually specify it.

# We can modify the above program as :

f = open("myfile1.txt", 'w')
data = ['This is line 1', 'This is line 2', 'This is line 3', 'This is line 4']
for d in data:
    f.write(d + '\n')
f.close()

# So yeah this much for today! Today we learnt about readlines and writelines in python file.io
# Tomorrow we will be learning about seek(), tell(), and other important functions in python

# Thank you! Happy coding!
    