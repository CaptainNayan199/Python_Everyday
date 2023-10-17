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

Ddc(Abc) #see here iam giving Abc function as an argument.
Ddc(Bbc) #passsing a function as an argument.

# Now lets see how a function can return a function

def div(num): # here i have a function with num as an parameter
    def divide(a): #inside i have another function, basically nested function
        return num/a # i am returning a value of a nested function
    return divide #this is returning the result of nested function
    

result = div(50) # here i have assigned div(50) into the result variable, as it has return type. 
# The nested function is still not being called, so still not executing.
print(result(5)) #here i have called the nested function and printed the result by passing the argument as well.

# So yeah this is it all about higher order function. Just remember higher order function is a function that either takes a function as an argument or returns a function.
# Thank you! We'll meet tomorrow. 