# Lambda functions are very important functions in python, they are single expressions
# They are used for writing anonymous functions
# Anonymous functions are those functions that has no any name

# Lambda functions syntax :  lambda arguments: expression

# Simple function with 2 parameters
def sum (a):
    return a+a
print(sum(2))


# Now rewriting this above function with the use of lambda kwyword

summ = lambda a,b: a+b
