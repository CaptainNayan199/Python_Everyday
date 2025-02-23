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
        elif user <answer:
            print("Too low! Try again!")
        elif user>answer:
            print("Too high! Try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses : {guesses}")
            is_running = False
    else:
        print("Please enter numbers only!")
        print(f"Select a number between {lowest} and {highest}: ")
