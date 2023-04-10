# Lists methods - here in this session we will be looking at some of the important lists methods that are very useful in manipulating certain lists
# They are very important lists methods as we have to perform various operations on lists in python

list1 = [1,2,3,4,5,6]
print(list1)
list1.append(7) #append methods adds elements in the list to the last.
print(list1)


list2=[45,325,2,12,5,435,1]
list2.sort() # sorts the elements of the list in ascending order
print(list2)

# But what if we want to print the elements of the list in reverse order

list2.sort(reverse=True) #sorts the data in descending order
print(list2)

list3 = [1,3,45,6,2,56]
print(list3,index(2)) #gives the indexing of the