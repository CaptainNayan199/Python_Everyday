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
        print("Today is Friday")
    case 7:
        print("Today is Saturday")
    case _:
        print("Invalid number provided! Please be responsible and provide a valid number [1-7] ")
        
        
# So this much for today class. Hope you got to know some new things today. 
# Practice more, remember the more you practice the more perfect you are going to be
#Tomorrow we will see about Loops in python. # # so yeah!Let's meet tomorrow.