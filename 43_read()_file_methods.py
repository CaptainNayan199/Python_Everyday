# So today we are going to see some important file methods in python like read(), readlines(), writelines() etc.

# readlines() methods - this methods is used to read a single line from the file, multiple lines can also be read by the use of loop

f = open("myfile.txt", 'r') #opening a file in read mode
while True: #using while loop
    line = f.readline() #using the readline method
    if not line: # if not is a special keyword in which checks whether the resepected line is there in the file or not and returns true if not found, else return false
        break #if not found
    print(line)
