#in this exercise we are trying to greet user either good morning, good afernoon, or good night 
# it will be decided as per the their inputs provided.
# we are using time package here in this exercise
# we are taking name as user input 

import time


hours = int(time.strftime("%I"))  # taking current time (in hour format, and formating it to int)
ampm = time.strftime("%p") # taking sm/pm information

name = input("Enter your name : ") #taking user input

if (hours >= 4 and hours <= 12) and ampm == 'AM': # using if conditions
    print("Hello ", name.capitalize(), "Good Morning.......")
elif (hours <=8) and ampm == 'PM':
    print("Hello ", name.capitalize(), "Good Afternoon.......")
else:
    print("hello ", name.capitalize(), "Good night.......")
