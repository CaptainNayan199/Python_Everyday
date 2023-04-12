# Today we are going to see about fstring in python languages.
# It is one of the best feature of python programming languages, and is appreciated by almost every py developers.
# This was released after py 3.6 version

# Fstring is string formatting in python languages, it is also one of the string methods in python
# So lets understand it with example]

name = "Nayan"
age = 20
color = "Red"
study = "BCA"

# So i have some variables with respective values, and now i can use it in this way : 

print("My name is ", name, " and I am ", age, " years old. My favorite color is ", color, " and currently i am studying ", study)
# But its hectic and quite long, everytime using double quotations and writing the variables 

# But what if we can write it in better way, lets see

print(f"My name is {name} and I am {age} years old. My favorite color is {color} and currently I am studying {study}") # this seems bit clear and easy to operate upon. 
# Hence, this is string formattting, its that simple

pi = 3.1415148796235892

# so here i have the value of PI, i can print it using simple print function, but what if i want to keep certain values after decimal, we can do it using f string

print(f"The value of PI is {pi:.2f}") # here, i have specified to keep upto 2 decimal places. So, yeah this is that simple