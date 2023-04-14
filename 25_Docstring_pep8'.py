# Docstring in pythons are the string literals that appears right after definition of functions, classes, methods, etc.
# Docstring are just like comments, they are ignored by the interpreter but they can be printed/invoked/ or whatever you say.

#using a docstring in functions - 
def cube (n):
    '''Hey this is my docstring, and I am inside a cube function. To use me please use  twice underscore doc twice underscore'''
    print(n*n*n)

cube(3)
print(cube.__doc__) #remember in function docstring must be defined before the body, and we can call the docstring using the method : function_name.__doc__ 