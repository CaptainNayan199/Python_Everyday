# So what are maps, filtering and reduce in python
# They are built in functions inside python programming language that basically allows us to apply a function to a sequence of elements and return a new sequence.
# They are called as higher order functions, why is so, will see later.

# Map functions - it is a function that applies a function to each element in a sequence and returns a new sequence as map.

# Syntax of Map function : 

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

# The output will be same in both case

