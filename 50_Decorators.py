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

def decor_func(func):
    def inside_func():
        print("Before hello this function is going to be shown")
        func()
        print("Now after hello this will be shown")