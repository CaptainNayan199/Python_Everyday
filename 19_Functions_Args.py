# Functions in python can be either with arguments or without arguments (parameters too; btw parameters and arguments are different things)
# Functional arguments are placed inside a small brakcets or ps: in python it can be given in form of sets, dictionaries too. (dont worry abt this things, we will see them in brief in upcoming sessions)
#  Lets see the different types of arguments in python programming

# 1. Default Argument 
def sum (a=3, b=4):
    print("Sum is ", a+b)
sum() # see it seems preety simple, which is btw, a sum function is made with 2 parameters a and b, and then sum is printed by calling the functions
# But if we pass any values to the function while calling the function like sum(4,5), it will get the first priority, then the sum will be 9 not 7

def name(fname, mname="Prasad", lname=""):
    print("Hey! ", fname, mname, lname)
name("Nayan", lname="Pathak") # Nayan Prasad Pathak

# 2. Keywords arguments - it is just a function with provided parameter, eg : sum(b=5, a=3)

# 3. Required arguments
def diff(a, b):
    print("Difeerence is ", a-b) # In this the arguments must be provided, or else it will throw an error
diff(5, 4)

# 4. Variable length arguments