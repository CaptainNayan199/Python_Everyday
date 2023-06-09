# Recursion is the method of repeating some task for n number of times, until the required or desired output is calculated.
# Recursion function are those types of function in python that keeps on calling itsefl until the desired output is met. So is done by calling the function.
# A recursive function should be able to call itself, have a proper stoppinfg condition or it will run infintely.

def factorial (n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1) # here the function is calling itself, so it is recursion

print(factorial(5)) #gives 120
print(factorial(1)) #gives 1 
     
# How it works : 
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 
# So this is how it works


# Generating fibonacci number : 
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))

# SO yeah this much for today, we will meet tomorrow, we will talk about recursion function in python.
# Thank you! Happy coding.