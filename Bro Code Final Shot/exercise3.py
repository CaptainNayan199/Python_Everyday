# compound interest calculator

# we need principal amount, time, and rate to calculate compound interest

principal = (input("Enter the principal amount : "))
time = (input("Enter the time : "))
rate = (input("Enter the rate : "))

while principal=="" or time=="" or rate=="":
    print("Please enter all the values carefully!")
    principal = (input("Enter the principal amount : "))
    time = (input("Enter the time : "))
    rate = (input("Enter the rate : "))

interest = int(principal) * pow((1 + int(rate)/100), int(time))
print(f"The compounded interest is : {interest:.2f}")