# Today in this session we will be looking at raising some custom errors in python
# someimtes we need to raise custom errors.
# we can use raise keyword in python.

# why to raise error? - to hault the program and not cause any further damages to the code or similar to it.

num = int(input("NUmber: "))
if num<18:
    raise ValueError("You are too small") # sp here i have raised a custom error, saying if user gives me his age less than 18, then i will give him an error by saying you are too small.
else:
    print("You are good to go")


# Unexpected errors or exception can be handled by the use of try, exception and finally keyword, likewise custom errors can be raised with the use of raise keywords.


# In python we can define custom exception by creating a new class that is derived from the built in exception class in python (we will see about class in upcoming session as well)

a = input("Enter any value between 5 and 9 : ")

if a == "quit":
    print("you choosed to quit") # if a person types `quit` then he is given some output
elif (int(a) < 5 or int(a) > 9):
    raise ValueError("Value should be between 5 and 9") # if the boundary is not met than this error is raised, it is a custom error.