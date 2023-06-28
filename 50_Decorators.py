# So what actually is decorators in python?
# They are special types of function that takes a function as an argument and is used to add more functionality to a function
# It is one of the most important features in python that allows us to modify the behavior of the methods, without actually modifying the methods.
# They change and return the function that is provided as arguments.

# They are a powerful and versatile tool that allows us to modify the behavior of the function and extend its functionality without modifying the code written in that module.

# It always returns a function 


# Basic syntax of the decorator function : 

# @decorator function #this decora
def func():
    pass

# The above line of code is shorthand for the following code:

def func():
    pass

func = decorator_function(func)



# Lets see with an example


# Here i have an simple function that prints hello world
def hell():
    print("Hello from the side of Nayan Pathak")

