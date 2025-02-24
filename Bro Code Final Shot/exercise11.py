# banking program

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amt = int(input("Enter some amount to deposit in the bank : "))
    if amt < 0:
        print("That's not a valid deposit")
        return 0
    else:
        return amt


def withdraw():
    print("Your current balance is : {}".format(balance))
    amt = int(input("Enter how much do you want to withdraw : "))
    if amt < 0:
        print("That's not a valid withdrawal")
        return 0
    elif amt > balance:
        print("You don't have sufficient balance!")
        return 0
    else:
        return amt

balance = 0
isRunning = True

while isRunning:
    print("*******************Welcome to the Nayan Banking App***************")
    print("1. Show Balance")
    print("2. Deposit Balance")
    print("3. Withdraw Balance")
    print("4. Exit")
    user = None
    while user not in ("1","2","3","4"):
        user = input("Enter any choice : [1-4]: ")
    if user == "1":
        show_balance()
    elif user=="2":
        balance += deposit()
    elif user=="3":
        balance -= withdraw()
    else:
        isRunning = False

print("Thanks!")


