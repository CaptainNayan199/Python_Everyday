# Lists in python are one of the most important data types 
# They are used to store multiple values
# They fall under the category of sequential data types as we have discussed in brief about all data types in past session
# Lists are nothing but just an order collection of data where each elements are seperated by commas and are enclosed within a square brakcets[]
# PS : Lists are mutable - i.e they can be changed later, are changeable and eidtableFiles Updated.
# There is a method called as 'append' which is used to add more elements to the lists
# Data inside a list can be of any types

listt = ["Nayan", "Pathak", 20, "BTM", False] #this is a list whose name is listt, and has multiple values with multiples data types
print(type(listt)) # prints the data types of the list

# Adding more values inside a particular list the use of append method

listt.append("Pokhara") #adds pokhara at the end of the list, and hence the new list will be : 
    #   listt = ['Nayan', 'Pathak', 20, 'BTM', False, 'Pokhara']

# List values indexing - the elements of the list are typically indexed starting from 0
 
lis = [1,2,3,4,5,6,7,8]
print(lis[0]) # 1
print(lis[1]) # 2
print(lis[6]) #7
print(lis[-2]) #7 - you can start negative indexing from the last

# finding certain elements in the list - 