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


# Here i have a decorator function that takes 1 arguments

def decor_func(func):
    # inside this function i will create another function that will be used to modify the contents of the function 
    def inner_func():
        print("Before hello world this will be printed")
        func() #the same function that has been passed as an parameter will be executed here
        print("After hello world this will be printed")
    return inner_func  #returning the inner function as decorator always returns a certain function



# A simple program that prints hello world

def hello():
    print("Hello world from ")
