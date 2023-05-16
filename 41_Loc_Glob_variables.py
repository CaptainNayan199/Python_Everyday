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
    print("My name is ", name) # here name is a global variable and it is files updated