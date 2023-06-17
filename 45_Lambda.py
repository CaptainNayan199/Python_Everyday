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






#  Using functions as arguments
summ = lambda a,b:a+b
def num(x,y):
    return x(y,y)+y
    
print(num(summ, 1))

