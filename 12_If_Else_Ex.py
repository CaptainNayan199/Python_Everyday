import time

hours = int(time.strftime("%I"))
ampm = time.strftime("%p")

name = input("Enter your name : ")

if (hours >= 4 and hours <= 12) and ampm == 'AM':
    print("Hello ", name.capitalize(), "Good Morning.......")