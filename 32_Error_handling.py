# Error handling is very important in any kinds of programming language
#Similiarly it is same for python language
# sometimes we knowingly or unknowingly are going to make an error, it can be because of user, or sometimes even because of server, so we can handle those errors in python language,
# we can use try and exception in python langugage to handle errors and exception.


a = int(input("A number please: "))
print(f"Multiplication table of {a} is : \n")
for i in range(1,11):
    print(f"{a} X {i} = {a*i}")
print("table has been printed")
print("Other code")

# so this is a simple program to generate multiplication table for any number in python
# there are no errors in the above program
# but if any errors can be occured in future, we can provide it in try and exception block
# lets see this : let us run my program, but if any errors are to arised, dont hault the program, run other lines of code
# Exception handling is the process of responding to the unwanted or expected events, where the program gets run
# exception  handling helps us deal with this types of exception or error


try:
    a = int(input("A number please: "))
    print(f"Multiplication table of {a} is : \n")
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except Exception as e:
    print("You have this error in your code : ", e)


# Even if errors appear in try block, this will not stop the program, rather if goes inside the except block as like in above program


# Handling specific errors : 

try: 
    #try block code here
    print("")
except ValueError:
     #handling value error
    print("")
except IndexError:
     #handling indexingf error
    print("")


# so this is how exception is handled in python programming language
# there are many other specific errors, that can be handled

# so yeah this much for today, today we talked about try and except in python, just remember whatever error comes in try block, the program immediately runs into except block
