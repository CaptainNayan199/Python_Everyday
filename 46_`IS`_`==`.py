# There is a keyword in python- is - what its use is? 
# What is the difference between is and == in python, do they have similar meaning?

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