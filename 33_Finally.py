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
