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

# As list or string concatenation, we can also concatenate two tuples, and make 3rd tuples.

tup1 = ("Nayan", "Pathak")
tup2 = ("Ujjwal", "Dhakal")
tup3 = tup1 + tup2
print(tup3)

# now lets see some of important methods in tuples

tup = (1,2,3,4,5,6,2,7,8,1,1,1)
print(tup.count(1)) # this methods counts particular elements in the tuples, so 1 has appeared 4 times in the tuples.

print(tup.index(2)) #this methods returns the first index of the respected elements. Remember I said first index, even if the element has appeared multiple times, it will return only the first index. 
# So here, it will say the index of 2 is 1

# We can even find the index of certain elements by slicing the tuples.

print(tup(2, 0, 7))  #this methods takes 3 arguements, the first one is the elements to search its index, and the other 2 arguments are the range for slicing

print(len(tup)) # this methods gives the length of the tuples.

# So yeah this much for today, we will meet up in tomorrows session.
# Thank you ! Happy coding.
