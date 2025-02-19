# a simple calculator made using python

# num3: int = int(input("Enter the first operand : "))

num1 = int(input("Enter the first operand : "))
num2 = int(input("Enter the second operand : "))
print("The available operator are : [ + , - , / , * , % ]")
operator = input("Select the operator : ")

if operator == "+":
    print("The addition between %s and %s is %s" %(num1, num2, (num1+num2)) )
elif operator == "-":
    print(f"The subtraction between {num1} and {num2} is {(num1-num2)}")
elif operator == "*":
    print("The multiplication between {} and {} is {}".format(num1, num2, (num1*num2)))
elif operator == "/":
    print("The result after dividing "+ str(num1)+ " by "+ str(num2)+ " is "+ str(num1/num2))
elif operator == "%":
    print("The remainder after dividing {a} by {b} is {c}".format(a=num1, b=num2, c=(num1%num2)))
else:
    print("Please select the appropriate operator.")