# Variable in python - variable in pythons are like a container that are meant to store something/values/data.

a = 1 # Storing 1 in a.
b = True 
c = "Nayan"
d = None 

# Data Types - data types specifies types of values that a variables is storing or holding.

a = 1 # Int data types
b = True # Bool data types
c = "Nayan" # String(Str) data types
d = None # # data type and an object of the NoneType class(we'll see about classes and objects later on dont worry !!)

# Knowing data types in python

a = 1 
b = True
c = "Nayan"
d = None
print(type(a), type(b), type(c), type(d)) #type is a function used to know the datatypes of variables in Python

# Built in data types in python :-

# 1. Number data types - int, float, complex

a = 1 # int data types
ab = 1.2324 # float data types
abc = complex(4,2)  # complex data types

# 2. Text data types - String ( Str) - they should be enclosed in either single or a double quotation mark.

c = "Nayan" # String data types 

# 3. Boolean data types - Bool

b = True # Bool data types - they determine either a statement is True or False
bcd = False

# 4. Sequence data types - list, tuple

# list - It is a order collection of data enclosed inside a square brackets and all elements seperated by a comma.
#        It is mutable. They can be again modified after they are created.

list1 = [5,2,"nayan","ram",["apple", "mango"]]
print(list1)

# Tuple - It is also a order collection of data with elements seperated by a comma and enclosed inside a parenthesis.
#         They are immutable and hence cannot be modified once they are created. 

tuple1 = (("lion", "tiger"), ("owl", "parrot"))
print(tuple1)

# 5. Mapped data types - mapping one things from other - dictionary

# dictionary/dict - It is an unordered collection of data containing a key:value pair. The key:value pairs
#                   are enclosed within a curly braces. 

dict1 = {"name":"Nayan", "surname":"Pathak", "age":20, "isMale": True}
print(dict1)
print(dict1.keys()) # knowing the keys of that dictionary
print(dict1.values())  # knowing the values of that dictionary

