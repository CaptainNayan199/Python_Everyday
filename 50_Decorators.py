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
@decor_func  #Now this one is very important, here we are saying our interpreter that decor_func is an decorator by using the @ symbol, the interpeter will understand it and pass the function that lies below the @decor_func as an parameter to the decorator function 
def hello():
    print("Hello world from the side of Nayan Pathak ")


# Now calling the hello function
hello()


# The output of the code above : 

# Before hello world this will be printed
# Hello world from the side of Nayan Pathak 
# After hello world this will be printed

# So this was all about decorator in python. Remember it is an very important feature in python programming.



 
