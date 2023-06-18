# So what are maps, filtering and reduce in python
# They are built in functions inside python programming language that basically allows us to apply a function to a sequence of elements and return a new sequence.
# They are called as higher order functions, why is so, will see later.

# Map functions 

def square(a): # a function that returns a square of a number
    return a*a


list1 = [1,2,3,4,5] # an list
sq_list = [] # an empty list
for i in list1: #calculating the square of a list using for loop
    sq_list.append(square(i)) #appending the square in new list
print(sq_list)
