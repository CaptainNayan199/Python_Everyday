#in this exercise we are trying to greet user either good morning, good afernoon, or good night 
# it will be decided as per the their inputs provided.
# we are using time package here in this exercise
# we are taking name as user input 
import time


hours = int(time.strftime("%I"))
ampm = time.strftime("%p")

name = input("Enter your name : ")

if (hours >= 4 and hours <= 12) and ampm == 'AM':
    print("Hello ", name.capitalize(), "Good Morning.......")
elif (hours <=8) and ampm == 'PM':
    print("Hello ", name.capitalize(), "Good Afternoon.......")
else:
    print("hello ", name.capitalize(), "Good night.......")
