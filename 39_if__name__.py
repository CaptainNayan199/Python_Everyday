# if__name__ == "__main__" is a very important pattern in python programming 
# A Python programme uses the condition if __name__ == '__main__' to only run the code inside the if statement when the program is run directly by the Python interpreter. The code inside the if statement is not executed when the file's code is imported as a module.

#  `if__name__` is a variable in python(inbuilt)

# Python has a large number of special variables that begin and end with double underscores. They are referred to as dunder to keep it brief (from Double Underscores). In this case, "__name__" is pronounced "dunder name."

# print (__name__) # - __main__ will be the output as we are in our main python file, not inside a certain modules

import time as time_package
print(time_package.__name__) # now here i have imported a time module as time-package. So whenever i print __name__ after importing certain module than i will get output as that particular module name . It is because i am imporing a module and i am working under same module

# The main job of __name__ keyword is to records the name of the currently running module or script.
# So in previous session we made a test python file and now lets see by importing it
