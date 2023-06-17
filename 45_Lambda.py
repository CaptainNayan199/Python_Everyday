# Lambda functions are very important functions in python, they are single expressions
# They are used for writing anonymous functions
# Anonymous functions are those functions that has no any name
# They are generally used to make mini and small functions like calculating area, sum, average, square and etc.

# Lambda functions syntax :  lambda arguments: expression

# Simple function with 2 arguments
def sum (a):
    return a+a
print(sum(2))


# Now rewriting this above function with the use of lambda kwyword

summ = lambda a: a+a #so this function has lambda keyword and then arguments, colon, and then expression respectively
print(summ(4))


prod = lambda a,b,c: a*b*c #it can even take multiple arguments and operate it accordingly

print(prod(2,3,4))


# PS: They are mostly used as passing parameter to a certain functions, yes a functions is passed as an argument to other functions, lets see by making a function and passing it as arguments.
#  Using functions as arguments

summ = lambda a,b:a+b # anonymous function

def num(x,y): #num function that returns sum of two numbers
    return x+y
    
print(num(summ(1,1),1)) # calling a function by passing summ function as a parameter


# OR
 
summ = lambda a,b:a+b
def num(x,y):
    return x(y,y)+y
    
print(num(summ, 1))


# So yeah this much for today
# Today we learned about lambda functions in python
# Tomorrow we will be talking about 

