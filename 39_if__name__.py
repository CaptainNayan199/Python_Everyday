# if__name__ == "__main__" is a very important pattern in python programming 
# A Python programme uses the condition if __name__ == '__main__' to only run the code inside the if statement when the program is run directly by the Python interpreter. The code inside the if statement is not executed when the file's code is imported as a module.

#  `if__name__` is a variable in python(inbuilt)

# Python has a large number of special variables that begin and end with double underscores. They are referred to as dunder to keep it brief (from Double Underscores). In this case, "__name__" is pronounced "dunder name."

# print (__name__) # - __main__ will be the output as we are in our main python file, not inside a certain modules

import time as time_package
print(time_package.__name__) # now here i have imported a time module as time-package. So whenever i print __name__ after importing certain module than i will get output as that particular module name . It is because i am imporing a module and i am working under same module

# The main job of __name__ keyword is to records the name of the currently running module or script.
# So in previous session we made a test python file and now lets see by importing it

import test as test_python_file
# Now under this file, i have 2 functions one is `sum` and the other one is `diff` 
# So now lets try to find the sum and difference of 2 numbers respectively

test_python_file.sum(10,2) # now it will give me result as Sum is 12

# Now if i do this than what happens ? 

if __name__ == "__main__":
    test_python_file.sum(10,2) # will this code run ?
#  The answer is NO, which is because inside if i have said if __name__ == __main__ then only run the code that is inside. 
# But here we are not doing operation with our main file, rather we are trying to work on certain module 

# Why this methods is important?
# this variable is important because this allows us to reuse the codefrom a script by importing it as a module in another program or script  

# python1.py : 
def main():
    print("This is in python1.py")
if __name__ == "__main__":
    main()

# python2.py
import python1
python1.main()

# This variable is generally important in such scenarios where we need to organize and seperate code that should be run directly from the code that should be imported and use as a module

# So in general this keyword is used to find whether the script is being run directly or is being sun by importing as a module into other script

# So yeah this much for today, today we learned about __name__ keyword in python
# Tomorrow we will be looking at OS module in python, dont miss it, its gonna be interesting.
# Thanks for watching. Happy coding!


