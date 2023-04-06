#functions in python are used to perform specific task whenever it is called

def f_name(): # function in python is defined using keyword def, after def function name is provided with parenthesis, remember there is no use of curly braces and semicolons so remember to add colons after parenthesis
    # Some block of lines
    # Some block of lines
    print("Hello")

# in like other programming language, calling a function is needed to sucessfully execute that particular function, so just write the name of the function and the function is called
f_name()


# In python empty function does not gets executed, but there is a magical keyword called as 'pass', which lets us run the empty function

def empty_function():
    pass

empty_function()


# There are 2 types of function in python programming languages

# 1. Built in functions - they are in build functions and are not required to invoke or create them. Eg : tuple(), hash(), set(), etc