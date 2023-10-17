# So today we are going to see about some higher order functions and what are they ?
# We all know that everything in python is treated as an object. So is functions.
# Higher order functions are those types of function in python where a function is accepting another function as an argument or is returning some function(ofcourse we have seen this in decorators as well, they return a function right?)
# So let's see with an example

def Abc(): #here i have one function
    print("This is Abc function")

def Bbc(): #here is the second function
    print("This is Bbc function")

def Ddc(func): #here i have 3rd function but it is taking one argument. 
    res = func() #the result of the func is being stored in res variable, and it will be displayed.
    print("This is Nayan accessing other function from Ddc")

Ddc(Abc)
Ddc(Bbc)

