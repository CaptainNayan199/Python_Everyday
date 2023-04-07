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
def averagee(*abc): #no worries mate this works as tuples ,  * represents a tuples where we can give many parameters as we want
    print(type(abc)) 
    sum = 0
    for i in abc:
        sum=sum+i
    print("Average is ", sum/len(abc))

averagee(1,2,3,4,5)
# PS: * Works as a Tuples, it represent a tuples

def average (**abc): # this works as dictionaries
    print(type(abc))
    print("I am" ,abc['name'], ". My college name is ", abc['college'], ". I am from ", abc['country']  )

average(name="Nayan", caste="Bahun", college="MMC", country="Nepal") # just an example, we will see in depth about each things in their respective session in coming future.
# PS: ** Works as Dictionaries, where data are provided in the form of key and their respective values

def aver(*avg):
    print(type(avg))
    sum = 0
    for i in avg:
        sum = sum + i
    averagee = sum / len(avg)
    return averagee

aver(1,2,3,4,5)

# Return - it is just what function is returning, or throwing back. In the above example the function is calculating the average and throwing it, remember it is not printing it.

# What happens if multiple returns are provided inside a function ?
# ==> The first return gets the top most priority and gets executed, rest others are just simply ignored by the interpreter as stepmom ignores her stepchildren(jk)

def abc():
    dif = 5-2
    return "First Return"
    return diff
abc()
# The first return gets executed.

# So yeah this much for today