# match case in python are similar to switch case in C.
# they are alternative to elif statements

day = int(input("Enter any day between 1-7 : "))
match day:
    case 1:
        print("Today is Sunday!")
    case 2:
        print("Today is Monday")
    case 3:
        print("Today is Tuesday")
    case 4:
        print("Today is Wednesday")
    case 5:
        print("Today is Thursday")
    case 6:
        print("Today is Friday")
    case 7:
        print("Today is Saturday")
    case _:
        print("Please enter a valid number between 1 to 7")