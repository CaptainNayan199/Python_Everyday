# while loop is used to execute some lines of codes, until the while condition remains true


# name = input("Enter your name : ")
# if name == "":
#     print("You did not entered your name")
# else:
#     print(f"Hello {name}")

# replacing the above if statements with while loops

# while name == "":
#     print("You did not entered your name")
#     name = input("Enter your name : ")
# print(f"Hello {name}")

# age = int(input("Enter your age : "))
# while age<0:
#     age = int(input("Please enter your age which is positive number : "))
# print("Your age is "+str(age))


# desire = input("Enter some of your hobbies [press q to quit] : ")
# while not desire == "q":
#     print(f"{desire}")
#     desire = input("Enter some of your hobbies [press q to quit] : ")
# print("You pressed q so we exited")

num = int(input("Enter any number between 1 to 10 : "))
while num<1 or num>10:
    print("The numbered you entered is not valid!")
    num = int(input("Enter the number again ! : "))
print("Finally you entered the correct number.")