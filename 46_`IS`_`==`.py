# There is a keyword in python- is - what its use is? 
# What is the difference between is and == in python, do they have similar meaning?

# The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory

# Main difference betwwen 'is' and '==' is that 'is' compares the exact location of the object in the memory, whereas '==' compares the values

# Both are comparison operator in python, used to compare 


a = 5
if a is None: # I am asking whether the value of a is None or not, where in this case it is not
    print(True)
else:
    print(False)


b = 4
if a==b: # i am comparing the values, whether the values of a and b are equal or not
    print("Yes")


a = 5
b = a
print(id(a))
print(id(b))
print(a is b) # compares the exact location in the memory
print(a == b) #compares the value


a = 5
b = 5
print(a is b) # returns True as both are pointing to the same objects which is 5
    