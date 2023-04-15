# SO what are sets in python ?
# Sets are just the collection of unordered objects/well defined objects.
# They dont take repeated values, and does not care about repeatation.

#  They are enclosed inside a curly braces, and are seperated by commas
# They are immutable, that means we cannot change the content of the set once we have created it.

set1 = {2,5,8,9}
print(set1)

set2 = {"Nayan", "23", "value", "this is set", False}
print(set2)
# set ignores the order, prints random values everytime.

print(set1[1]) # throws error
# PS : We cannot access the values of the set by the use of indexing methods.

empty = {}
print(type(empty)) # this will give a dict data types, not set, it is a dictionary

# we can create an empty set by using a keyword set

empty_set = set() #remember not a curly braces
print(type(empty_set)) # this will give us a set data types

set5 = {1,2,3,4,5,6,7,8,9,"Nayan"}
for i in set5:
    print(i)


