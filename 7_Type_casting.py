# Type casting in python - It is the conversion of one data type into another data types.

# Python supports variety of functions and methods for type casting like : 
# int(), float(), Str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc.

# A simple example of type casting
a = int(input("Give me a number "))
b = int(input("Give me second number "))
div = a/b # It will give float value.
print(div)
div = int(a/b) # It will give int value. So it is type casting, we have converted a float data type value to int
print(div)


# There are two types of type casting in python

# 1) Explicit Type casting - This type of type casting is done by the programmer or the developer themselves.
# It is done manually as per the requirements of the program. This type casting can be obtained by using methods
# like int(), float(), Str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. Example:

a = 12.67
print(a) # It gives float value of a
print(int(a)) # It gives integer value of a

# 2) Implicit Type casting - This type of type casting is done by the python interpreter itself. It is done 
# automatically. Implicit type casting is done to prevent data loss. Example:

a = 7 # Python automatically converts a to int
print(type(a))
b = 3.0 # Python automatically converts b to float
print(type(b))

c = a + b # Python automatically converts c to float as it is a float addition
print(c)
print(type(c))
 
d = a * b # Python automatically converts d to float as it is a float multiplication
print(d)
print(type(d))


#typecasting is very useful function in python
# remember one thing, the input from user always come in string format in python and hence 
# as per need you need to convert it to other data types (especially int)

# for example

user_input = input("Please say anything please : ") #so this is just a simple way to get user input
#but this input is in string format as you can see below 

print(type(user_input))  #this gives you information about the user_input data types which is obviously non other than String

#so to make this int you can type cast it as shown below

user_input = int(input("Please say something please : ")) #so this is a integer output 
# we just typecasted it
# in a similar manner, you can type cast it as per your need.