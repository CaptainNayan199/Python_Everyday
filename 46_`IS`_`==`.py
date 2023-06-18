# There is a keyword in python- is - what its use is? 
# What is the difference between is and == in python, do they have similar meaning?

# The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory

# Main difference betwwen 'is' and '==' is that 'is' compares the exact location of the object in the memory, whereas '==' compares the values

# Both are comparison operator in python, used to compare 


a = 5
if a is None: # I am asking whether the value of a is None or not, where in this case it is not
    print(True)
else:
    print(False)


b = 4
if a==b: # i am comparing the values, whether the values of a and b are equal or not
    print("Yes")


a = 5
b = a
print(id(a))
print(id(b))
print(a is b) # compares the exact location in the memory
print(a == b) #compares the value


a = 5
b = 5
print(a is b) # returns True as both are pointing to the same objects which is 5
    

a = [1,2,3]
b = [1,2,3]
print(a is b) # returns False, dont get confused, yes it returns false.Why ? lets see

# So whata actually happens is, a = 5, here we are defining an variable who value is 5, python assumes this is constant and hence, it only assigns a single memory for it, and then it any other variable like b = 5, is defined, python will say 5 is already there, so no need to use more memory, rather lets directly point to the previous 5, python thinks 5 is immutable

# But for the list, list are mutable, so python will assign memory blocks respectively as per the list, if there are  list with same elements, python will independently assign them into the memory as it knows list can be changed.

tup1 = (1,2,3,4,5)
tup2 = (1,2,3,4,5)
print(tup1 is tup2) # returns True because tupple is immutable, so why to keep same tuples in 2 different memory location, rather keep one tuple in one memory location and point the other tuple to that memory location


# So this was the difference betwwen is and ==, is compare for identity, location, in the memory objects, but == comparess only the values.