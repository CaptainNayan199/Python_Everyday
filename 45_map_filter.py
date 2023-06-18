# So what are maps, filtering and reduce in python
# They are built in functions inside python programming language that basically allows us to apply a function to a sequence of elements and return a new sequence.
# They are called as higher order functions, why is so, will see later.

# Map functions - it is a function that applies a function to each element in a sequence and returns a new sequence as map.

# Syntax of Map function : 

from pickle import REDUCE


map(function, iterable) #iterable = any iterable objects like list, etc.

def square(a): # a function that returns a square of a number
    return a*a


list1 = [1,2,3,4,5] # an list
sq_list = [] # an empty list
for i in list1: #calculating the square of a list using for loop
    sq_list.append(square(i)) #appending the square in new list
print(sq_list)

# The above mentioned way is hectic and longer, lets calculate square of the list using map

sq_list2 = []
sq_list2 = map(square, list1) # using map function, that takes 2 arguments, one is function and other one is the value of the list
sq_list2 = list(sq_list2) # converting it into list
print(sq_list2) 

# The output will be same in both case, so it is the use of Map in python

# Filter functions - as name suggests, this function is used to filter a sequence of elements based on a given predicate(a function that returns either true or false), and returns a new sequence that meets the predicate

# Syntax of the filter function - 

filter(predicate, iterable)


list1 = [1,2,3,4,5] #new list

def func(a):
    return a>3 # a fiunction that returns true if a>3 else returns false

list2 = list(filter(func, list1)) #use of filter, filtering is done as per the the parameters provided, the func gets the parameter from list1, and then those values that satisfies the function condition are added in list2.
print(list2) #print the list2


# age = [23,12,56,83,2,3,6,12,19]
age = []
for i in range (10):
    a = int(input("Enter ages : "))
    age.append(a)

def check(a):
    return a>18

list2 = list(filter(check, age)) # age goes as parameter for the check function 
print(list2)
for i in list2:
    print(f"Hey you are qualified to drive as your age is {i} which is greater than 18")


# Reduce functions - It is an higher order function that applies a function to a sequence and returns a single value
# BUT : PS: before using reduce, we need to import it as : from functools import reduce & reduce most of the time takes a function that takes 2 arguments.
# Syntax of Reduce function -

REDUCE(function, iterable)


from functools import reduce
age = [23,12,56,83,2,3,6,12,19]

def sum(a,b):
    return a+b

list2 = reduce(sum, age) #So what reduce does is : basically takes first two numbers from age 23, 12, pass it as parameter to the function sum, stores it, again takes another number 56, and the previous output, and pass it as parameter again, and so on....
print(list2)
