# variable scope is a place where a variable is visible and accessible.
# scope resolution = Local, Enclosed, Global,Built-in # that is the local variable will be used first, and then enclosed, and then global and then built in

def add():
    a = 2
    b = 3
    return a+b
# a and b are local variable to the function add

def sub(x, y):
    x = 3
    y = 2
    return x-y
# x and y are local variable to the function sub
