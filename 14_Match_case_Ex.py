# in this simple exercise we will be using match case logic to determine certain day as per user input
# first of all we will take  integer user input and then determine on the basis of it

week = int(input("Please enter a number between 1 to 7 : "))
match week:
    case 1:
        print("Today is Sunday")
    case 2:
        print("Today is Monday")
    case 3:
        print("Today is Tuesday")
    case 4:
        print("Today is Wednesdays")
    case 5:
        print("Today is Thursday")
    case 6:
        