# So today we are going to see some important file methods in python like read(), readlines(), writelines() etc.

# readlines() methods - this methods is used to read a single line from the file, multiple lines can also be read by the use of loop

f = open("myfile.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
