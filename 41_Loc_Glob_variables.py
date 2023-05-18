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

# What if we try to change the value of the global variable 





