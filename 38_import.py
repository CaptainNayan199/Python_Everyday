# So today we are going to observe what actually is import and how does it work
# what is the rocket science behind it?

# so whenever we want to use any libraries in python, we need to install it using pip command, and then after installing it we need to import in our code and then only we can use it.
# IMporting in oython is the process of loading code from a python module in the current code. This allows us to use the function and variables defined in the module in your current code, as well as any aditional modules that the imported module may depend on.

# How to import a module or certain package in python?
# First and foremost we need to install the required module using pip command
# pip install pandas

# now pandas have been installed in our local system, to use it we need to import its

# in our script, at the top we need to type - import module_name; so in our case import pandas
# Remember we should import it at the top of our python script


# From keyword in python - This keyword is used to import only a specified section in certain module
# Eg - pip install math - i have imported a python module named math
from math import pi # - so with the use of from keyword, i have imported a specified functions from the math package 
# so from keyword is used to import certain or specified functions or variables from a module

# Importing everything with the use of * - this is used to import all the functions inside a certain modules

from pandas import * # so here  i have imported all the contents either functions or variables from the modules named pandas. So it is how importing all the functions/variables can be imported using * keyword

# But this is not recommended because it can create confusion