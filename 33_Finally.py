# Previously we talked about error handlign by the use of try and except block
# So today we will be talking about finally keyword in python
# We can use finally with try and except keyword
# PS : Whatever the code is, or whatever error the code is having, finally always runs, no matter what.

try:
    a = 5/0
except Exception as error:
    print("You have error in your try block : ", error)
finally:
    print("This is finally and it always gets executed no matter what")

# Here we have error in our code, and the error is we are dividing a number by 0, which is practically impossible, hence it throws error, but the finally statement always runs despite of error

# A finally clause is always executed before leaving the try statement, whether an exception has occurred or not. When an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in a except or else clause), it is re-raised after the finally clause has been executed. - REMEMBER THIS STATEMENT  

# Execution flow of try, except and finally in python : 

# `If there is no error produced by the try block: `
# 1. Execute statements in try block
# 2. Execute and return value from finally 
# 3. Return value from try block

# `If there is error produced by the try block: `

# 1. Execute statements in try block
# 2. Execute statements in except block
# 3. Execute and return value from finally block
# 4. Return value from except block

# Example to illustrate above statement, try running by giving an error, and without giving and error

def function1():
   try:
         num = int(input("Numbers : "))
         return num
   except Exception as error:
         print("You have error in your try block : ", error)
         return "exception"
   finally:
         print("This is finally and it always gets executed no matter what")
value = function1()
print(value)

# Try understanding the above code output and the flow of the try, except, and finally block when there is error, and when there is no error.

# So yeah this much for today! Today we learned about finally keyword in python, and it is very important topic in python

# Tomorrow we will be learning about raising custom (own desired errors)

# Thank you! Happy coding!

