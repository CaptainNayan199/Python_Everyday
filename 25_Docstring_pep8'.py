# Docstring in pythons are the string literals that appears right after definition of functions, classes, methods, etc.
# Docstring are just like comments, they are ignored by the interpreter but they can be printed/invoked/ or whatever you say.

#using a docstring in functions - 
def cube (n):
    '''Hey this is my docstring, and I am inside a cube function. To use me please use  twice underscore doc twice underscore'''
    print(n*n*n)

cube(3)
print(cube.__doc__) #remember in function docstring must be defined before the body, and we can call the docstring using the method : function_name.__doc__ 

# Docstring are not like comment, btw they are given special treatment by the interpreter.
# Docstring are written just above the function body and it is used generally to document you code, and used with the use of doc attribute.
# PS : remember they are not comment.

def sum (n):
    print(n)
    '''Now this is not a docstring as it is not exactly above the function body'''
    print(n+n)

sum(2)
# so if you want to print the docstring now, it wont be printed.
print(sum.__doc__) #this will return a none output

# PEP-8 - PEP 8 (Python Enhancement Proposals) is a document written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan that provides guidelines and best practices on how to improve the readability and consistency of Python code.