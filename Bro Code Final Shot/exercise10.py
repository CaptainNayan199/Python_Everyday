# rock paper scissor

import random
rpc = ("Rock", "Paper", "Scissor")
comp = random.choice(rpc)
user = None
isPlaying = True

while isPlaying:
    comp = random.choice(rpc)
    while user not in rpc:
        user = input("Please select any between [ Rock | Paper | Scissor ] : ")
    if comp == user:
            print(f"You chose : {user}")
            print(f"Computer chose : {comp}")
            print("Draw!")
    elif comp == "Rock" and user == "Scissor":
            print(f"You chose : {user}")
            print(f"Computer chose : {comp}")
            print("Computer Won!")
    elif comp == "Paper" and user == "Rock":
            print(f"You chose : {user}")
            print(f"Computer chose : {comp}")
            print("Computer Won!")
    elif comp == "Scissor" and user == "Paper":
            print(f"You chose : {user}")
            print(f"Computer chose : {comp}")
            print("Computer Won!")
    else:
            print(f"You chose : {user}")
            print(f"Computer chose : {comp}")
            print("You Won!")
    is_Play = input("Do you want to play again ? [Y/N] : ")
    if is_Play == "Y":
        isPlaying = True
    else:
        isPlaying = False
