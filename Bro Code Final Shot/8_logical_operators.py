# Logical operators in python are AND, OR, and NOT
# AND - all the conditions must be true
# OR - at least on of the condition must be true
# NOT - inverts the conditional boolean value(true to false, and false to true)

# age = 19
# isStudying = True
#
# if age<18 and isStudying:
#     print("You are a kid!")
# elif age>18 and not isStudying:
#     print("You have completed your studies!")
# elif age > 18 or not isStudying:
#     print("At least one of the above condition remains true")
# else:
#     print("Nothing to show")

user_input = (input("Enter your boolean value and i will revert it and display you : "))
if user_input == "True":
    print(False)
else:
    print(True)