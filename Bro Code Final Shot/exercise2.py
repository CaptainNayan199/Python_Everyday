user_input = input("Enter any thing as user input : ")

if len(user_input) > 12:
    print("You cannot have more than 12 characters")
elif user_input.count(" ") >= 1:
    print("Sorry you cannot include spaces there!")
elif not user_input.isalpha():
    print("You cannot include digits there as of now!")
else:
    print("You have passed all the test successfully!")