# Tuples is also one of the most important sequential data types in python
# It is equally important as lists, and dictionaries(we'll talk abt it in future session).
# They are order collection of data with each elements seperated by commas, and enclosed within parenthesis.
# PS : Lists are enclosed inside a square brakcets, and TUples are enclosed inside a small brakets.

# PS : Tuples are immutable data types in python.
# That means once they are created, they cannot be changed or modified further unline lists which are mutable.
# Once a Tuple is created, it cannot be modified or changed further.

# eg : 
tuples1 = ("nayan", 1, 34, "pathak")
print(tuples1)
print(type(tuples1))

tup = (1)
print(tup)
print(type(tup)) # it will say it is int, because it is just a single value, if we want to create a tuple of single value than it is necessary to add a commaa after that value
# Eg :

tupp = (1,) # now this is a tuple with one value

newtup = (1,2,3,4,6,7)
print(newtup)
newtup[3] = 88 #this will throw a error as we have discussed earlier that tuples after creating once cannot be changed further
print(newtup) #it will throw error

# If we want to create a list of elements that should not be changed for lifetime, then we should make a tuples in that case

# ELements in the tuple can be anything like int, string, bool and etc

newtupp = (1,2,3,4,6,7,"Nayan", "pathak", True)
print(newtup, type(newtup))
# Index values can also be printed in below fashion, it is same as that in lists
print(newtup[0])
print(newtup[1])
print(newtup[2])
print(newtup[3])
print(newtup[4])
print(newtup[5])
print(newtup[6])

print(newtup[30]) # this will throw error as value at index 30 is not there in the tuples

# Negative indexing is alos same as that in lists, and strings

print(newtup[-2]) #this will give output = len(newtup) - 2 = 7, so it will give the value at 7 position  which is Pathak

# checking if particular value is in the given list or not

tt = (1,2,3,4,5,6,"nayan", "baby")

if 30 in tt:
    print("Yes it is there")
else :
    print("Sorry! not found")
# it will say sorry as 30 is not in the provided tuples

# Same goes for some string too

if "nayan" in tt:
    print("Yes")
else:
    print("No")