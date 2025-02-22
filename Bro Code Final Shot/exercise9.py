# random number guessing game

import random

lowest = 1
highest = 50
answer = random.randint(lowest, highest)

guesses = 0
is_running = True

print("::::::::::::::::::::::::::::::::::::")
print(f"Select a number between {lowest} and {highest}: ")

while is_running:
    user = (input("Enter your guess : "))
    if user.isdigit():
        user = int(user)
        guesses +=1

        if user < lowest or user>highest:
            print("Only enter the guess in between {} and {}".format(lowest, highest))
    else:
        print("Please enter numbers only!")
        print(f"Select a number between {lowest} and {highest}: ")
