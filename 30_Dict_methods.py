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



