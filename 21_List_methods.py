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
print(list3,index(2)) #gives the indexing of the element 2 which is non other than 4

list3 = [1,3,5,6,7,8,1,1,12]
print(list3.count(1)) #counts the repeatation of the certain elements. Eg : 1 has occured 3 times so it will give output 3.

list4 = [1,2,3,4,5]
list4.insert(1,2) #inserts the new values to the provided destination, has two parameters: destination, new values
print(list4)

list5 = [6,7,8,9,10]
list4.extend(list5) #extends(concatenate)/ add another list elements to the end of the list
print(list4)
# But the previous list value will be now changed as we have added some more elements by concatenating other list

# What if we want to keep the previous list values and concatenate
# Simply creating a new list and adding the value of two list, in that particular list, this will not hamper the original list elements

# Eg:   
new_list = list4 + list5 #creating a new list and adding the other list value to concatenate and make a single list, in this the previous list elements will not get erased.
print(new_list)

# LIke wise there are many list operations and methods in pythons, but these are few that are very important, and one must be familiar with these methods.

# So yeah this much for today session