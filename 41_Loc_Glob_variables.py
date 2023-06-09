# So today we are going to see about local and global variables
# We will also see about the use of global keyword, when to use it

# So firstly lets see it in simple terms

# Local variables are those variables that can be used/that are used inside a some variable or module

def function():
    name="Nayan"
    print("My name is ",name) # so here name is my local variable, i cannot access it outside of function


# Likewise, Global variables are those variables that are accessbile everywhere

name = "Ujjwal"

def function_2():
    print("My name is ", name) # here name is a global variable and it is being used inside of a function


# So, Global variable are those variables that are define out of any functions and are accessible through out the script i.e we can use this variable both in inside as well as outside of the function

# But the case for local variable is different as talked earlier, local variables are defined inside of certain functions and are accessbile only inside of that functions

# let's see by using a local variable outside of function

# So here I have created a function named namee. It has certain local variable 
def namee():
    name = "Nayan Pathak"
    age = 20
    isMarried = False
    isStudent = True
    print(f"My name is {name} and my age is {age}. My marrital status is {isMarried}.")
namee()

# Now lets see accesing the local variable outside of certain function

print(f"My name is {name} and my age is {age}. My marrital status is {isMarried}.")

# Here we will get an error
# Error is : 
# ERROR!
# NameError: name 'name' is not defined. Did you mean: 'namee'?

# So we got clear that local variable can aonly be accesed inside their particular function

age = 15
def namee():
    age = 20
    print("Your age is ", age) # here the output will be 20, coz local variable gets priority
namee()

print("Your age is ", age)

# What if we try to change the value of the global variable using the local variable, we will get an error

# Use of global variable in the python script

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# This global keyword is used primarily when there is a need of using the variable outside the function 

s = 5

def name():
    s = s+5 #here we have tried to change the value of the global variable using the local variable
    print("The local variable is : ",s) # this will give us error, as we are trying to edit the value of the global variable

name()

print("The global variable is : ", s) # this gives us output as 5 as this is accesing the global variable

# So in above case when we call the function we will get an Error as `UnboundLocalError: cannot access local variable 's' where it is not associated with a value`

# Now for solving the above problem we need to make sure that we are using the Global keyword in our program


s = 5

def name():
    global s
    s = s+5
    print("The local variable is : ",s)

name()

print("The global variable is : ", s)
# now this will print the value of the variable s as 10, both inside of the function as well as outside the function.
# Basically the use of global keyword is when there is a variable made inside a function and that needs to be use outside of the function.

# So yeah this much for today, today we talked about local and global variable and its uses. 
# Tomorrow we will be looking at file IO in python

# Thank you! Happy coding!
    





