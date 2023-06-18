# There is a keyword in python- is - what its use is? 
# What is the difference between is and == in python, do they have similar meaning?

# Main difference betwwen 'is' and '==' is that 'is' compares the exact location of the object in the memory, whereas '==' compares the values


a = 5
if a is None: # I am asking 
    print(True)
else:
    print(False)