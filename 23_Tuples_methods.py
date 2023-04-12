# Today we will talk about some of methods present in tuples in brief.
# we cannot change the values inside a tuple directly as tuples are immutable.
# Hence, we need to see some indirect way for modifying tuples.


# PS : if you want to add, edit, or remove the contents of the tuples than we must first convert that particular tuples into list and then we can perform necessary operations and then again we can convert it into tuples.

# See this example in brief : 
# creating a new tuple
tuple1 = ("Nayan", "Ujjwal", "Birendra", "Sita","Gita", "Neeta", "Neha")

# change the tuple into a list by using a secondary variable

list1 = list(tuple1)

list1.append("Kishan") #adding two elements to the list
print(list1)

list1.append("Nimmee")
print(list1)

list1.pop(4) # this will pop the element at index value 4

list1[1] = "Nayan" #replacing nayan in index 1
# So we can perform many operations in the tuple after changing it to list
tuple1 = tuple(list1) #further changing list into tuples.
print(tuple1)

