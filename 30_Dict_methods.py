# So today we will be discussing about some of the methods available in dictionary

#Here i have dictionary holding some information about a guy named Nayan.
dic = {
    "Name": "Nayan",
    "Aim": "Pilot",
    "Age":20,
    "isMarried": True,
    "Friend": "Suman"
}

dic2 = {
    "College": "TU",
    "Hobby": "Nothing"
}

# Now what if i want to update my dictionary
print(dic)
(dic.update(dic2)) # this will add all the key value pairs to the `dic` dictionary
print(dic)

# clear() - it is used in clearing all the dictionary

print(dic.clear()) #returns None value as the dict has become empty now.

#creating empty dict : 

empty = {}
print(empty) #empty dict

# pop() - retrieves a single key value pair

print(dic)
dic.pop("Name") #pops out the Name key with its value.
print(dic)

dic.popitem()
print(dic) # this method pops out the last key value pair

# del - deletes the entire dict.

del dic["Nayan"] # deletes only the key Nayan with its value, not the entire dictionary

del dic # deletes the entire dictionary
print(dic) # throws error.

# So yeah this much for today, there are many many and many methods, which i cannot cover all in a single file, you can visit python language documentation and read them, python docs are very very friendly

# Tomorrow we wil see about forloop with else in python

# Thank you! Happy coding!





