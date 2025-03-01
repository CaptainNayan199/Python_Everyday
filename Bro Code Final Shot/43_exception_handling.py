# exception is an event that interrupts the flow of a program
# we use try, except and finally in python for exception handling


try:
    num = int(input("Enter eny number : "))
    print(num/0)

except ZeroDivisionError:
    print("Sorry you cannot divide a number by 0")

except ValueError:
    print("Enter only number please")

except Exception:
    print("Sorry! Something went wrong")

finally:
    print("Finally always keeps executing!")

