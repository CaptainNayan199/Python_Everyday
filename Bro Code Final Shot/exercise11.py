# banking program

def show_blnc():
    pass

def deposit():
    pass

def withdraw():
    pass

balance = 0
isRunning = True

while isRunning:
    print("Welcome to the Nayan Banking App")
    print("1. Show Balance")
    print("2. Deposit Balance")
    print("3. Withdraw Balance")
    print("4. Exit")
    user = None
    while user not in ("1","2","3","4"):
        user = input("Enter any choice : [1-4]: ")
    if user == "1":
        show_blnc()
    elif user=="2":
        deposit()
    elif user=="3":
        withdraw()
    else:
        isRunning = False


