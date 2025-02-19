# conditional expression in python are used to evaluate an expression, check any condition in one line, they are basically ternary operator in python
# prints one value if first condition is true, else prints another value if false
# Syntax - x if condition else y

# num = int(input("Numer : "))
# print("Positive number" if num>0 else "Negative number" )

#
# num = int(input("Numer : "))
#
# print("Even number" if num%2 == 0 else "Odd number")


user_role = input("Enter your role : [Teacher / Student] ")
print("You are allowed to enter the system" if user_role.lower() == "teacher" else "You are not allowed to enter the system")
