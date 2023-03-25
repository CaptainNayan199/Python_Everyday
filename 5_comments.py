# comments in python - comments in python are used to say what does the code means. It is the line which does not 
# gets recognized by the compiler and interpreters. Comments are written to show what does that particular code 
# means.

# please remove this line ok after sometime
print("Hey I am a good boy.\nand he is also a good boy.")

print("This is inline comment")   # this is inline comment


'''
this is a milti-line comment   

'''

# Escape sequence - is a backslash followe by a character you want to install, cant be directly used as string.

# \n - new line escape sequence

print("Nayan\nPathak")


# anything inside (\"........\") goes into double quotations 

print("Hey my name is \"Nayan Pathak\"\n and iam a student")
print("\"My \'name' is Nyana\"")

# print statement in python
# Print statement is used to give output in python. print()

print("Nayan")  # string value in print statement
print(20) # integer value in a print statement
print("Nyana",1,3,"Pathak")  # Multiple values in a single print statement

# Seperator and ending in python

# Seperator is used to seperate multi line values inside a print statement.

print("Nayan","Pathak", sep="*") # here seperator is a star. So, it will give Nayan*Pathak as output.
print("Hi",1,2,sep="A") # here seperator is a alphabet A. So, it will give output - HiA1A2a
print("Hi",1,2,sep="/") # here seperator is a divide sign. So, it will give output - Hi/1/2

# Ending is used to append something to the end of a print statement.

print("Nayan",1,"A",sep="*", end="01") # output - Nayan*1*A01 - Here 01 gets appended at the end.
print("Nayan",1,"A",sep="*", end="01")
print("Hello") # output - Nayan*1*A01Hello - Here 01 gets appended at the end and Hello is printed.
print("Nayan",1,"A",sep="*", end="01\n")
print("Hello") # output - Nayan*1*A01 plus new line and in a new line Hello gets printed.
               #          Hello