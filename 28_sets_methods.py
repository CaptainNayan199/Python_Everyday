# In previous session we talked about sets, and today we are going to see about some important sets methods.
#they work in same ways as sets in mathematics.

set1 = {1,2,3,4,5}
set2 = {5,6,7,8}
print(set1+set2) # this is not the way to perform set operations
# well lets see some of the operations that can be performed in the set like union, intersection, etc.
#union
print(set1.union(set2)) #this gives the union of two sets.

print(set1.intersection(set2)) #this gives intersection of two sets.

(set1.update(set2)) # this method is saying that update the value of set1 i.e put every unique values of set2 in set1. SO our output will be: 1,2,3,4,5,6,7,8
print(set1)

s1 = {"Nayan", "Ujjwal", "Roshan", "Santosh", "Tika"}
s2 = {"Tika", "Prateek", "Kushal", "Messi"}
print(s1.union(s2)) #this does union operations
s1.update(s2) #this does adding unique values from s2 to s1.
# PS: Dont get confused in between union and update, update does changes the previous values, but union does not, if referenced using  3rd variable then it can but usually inside a print statement, it does not

print(s1,"\n", s2)

# Symmetric difference : this is deleting the intersection/ or the same values from two sets.

s1 = {"Nayan", "Prateek", "Roshan", "Santosh", "Tika"}
s2 = {"Tika", "Prateek", "Kushal", "Messi"}
print(s1.symmetric_difference(s2)) # so basically it deletes the same values from two sets, i.e in s1 and s2; Tika, and Prateek are identical so hence it deletes those values and prints the remaining elements from both the sets. Hence, our final output will be : Nayan, Roshan, Santosh,Kushal, Messi.

# PS : Dont worry about orders, set does not care about Orders, kinda like bad boy(hehe)

# Difference : The difference of two sets, written A - B is the set of all elements of A that are not elements of B.

a = {2,4,6,8,10}
b = {2,4,6,8}
print(a.difference(b)) # so this deletes all the repeated values from two sets and prints the remaining elements, so our output will be 10

s1 = {"Nayan", "Prateek", "Roshan", "Santosh", "Tika"}
s2 = {"Tika", "Prateek", "Kushal", "Messi"}
print(s1.difference(s2)) 

#Symmetric difference : Symmetric difference is simple; first it calculates the difference between two sets, and then gives out the remaining elements from both the sets.

s1 = {"Nayan", "Prateek", "Roshan", "Santosh", "Tika"}
s2 = {"Tika", "Prateek", "Kushal", "Messi"}
print(s1.symmetric_difference(s2))


# PS : difference gives us the remaining elements from the set that we are calulating the difference of; for eg : A-B , here only remaining elements from A will be printed, but in symmetric, A-B; all the remaining elements of both A and B will be printed.

s1 = {2,4,5,6,7}
s2 = {2,4,6,7,8,9}
print(s1.symmetric_difference(s2)) #gives us 5, 8, 9


# The intersection_update() finds the intersection of different sets and updates it to the set that calls the method.

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

# updates set A with the items common to both sets A and B
A.intersection_update(B)

print('A =', A)

# Output: A = {2, 3, 4}

#Symmetric_difference_update: this method assigns/update the given sets with the new value

s1 = {"Nayan", "Prateek", "Roshan", "Santosh", "Tika"}
s2 = {"Tika", "Prateek", "Kushal", "Messi"}
print(s1.symmetric_difference(s2)) #this will give symmetric difference
s1.symmetric_difference_update(s2)
print(s1) #this will also calculate the symmetric difference but modifies/update the values of s1 with the new symmetric difference value


#Some in build methods in sets in python

#superset and disjoints

s1 = {1,2,3,4,5,6}
s2 = {8,9,10}
print(s1.isdisjoint(s2)) # returns True as there are no any elements common in both the set.

s1 = {1,2,3,4,5,6}
s2 = {3,4,}
print(s1.issuperset(s2)) # return True as elements of s2 falls under s1, so s1 is a subset of s2.


print(s2.issubset(s1)) #returns true as s2 is a subset of s1, as every elements of s2 are in s1.


#add() methods - adding single items in sets

s1 = {1,2,3,4,5,6}
s2 = {3,4,}
(s1.add("Nayan"))
print(s1) #this methods add the new elements, in the set
#PS: add methods allows adding only single items at a time.

#PS : if we want to add multiple value then we can use the update method which we have discussed earlier.

#remove and discard method()

s1 = {1,2,3,4,5,6}
s2 = {3,4,}
(s1.add("Nayan"))
print(s1)
s1.remove("Nayan") #this methods removes Nayan from the set
print(s1)

s1 = {1,2,3,4,5,6}
s2 = {3,4,}
s1.discard(1) # discards 1 from the set
print(s1)

#PS: remove and discard same as well as not same also in python, if we try removing the element that is not in set, then it will throw error, but if we try discarding element that is not present in set then it will not throw error.

s1 = {1,2,3,4,5,6}
s1.discard(100)
print(s1) #this will not throw error, if matching elements is found then it removes or else it continues.
s1.remove(100)
print(s1)  #this will throw error, if matching element is found then it will remove it, else it will throw error.

#pop() methods - thie methods pops the random elements from the set, we can retrieve that element by storing it in a random variable.

s1 = {"Nayan", "Tika","Nishan", "Roshan", "Santosh"}
s2 = s1.pop()
print(s2)
print(s1)

# as set does not care about order, there is equal chance where the element that gets popped in first does not get popped in second.

#del() - it is basically a keyword, not a method in set, it can be used to delete a set.

s1 = {"Nayan", "Tika","Nishan", "Roshan", "Santosh"}
print(s1)
del s1
print(s1) #this will throw an error saying s1 has not been defined.

#clear()- this methods deletes the entire elements of the set, i.e it makes the set empty.

s1 = {"Nayan", "Tika","Nishan", "Roshan", "Santosh"}
s1.clear()
print(s1) #returns set()- as it has become an empty set now





