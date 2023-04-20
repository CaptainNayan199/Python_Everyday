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


# PS : difference gives us the remaining elements from the set that we are calulating the difference of; for eg : A-B , here only remaining elements from A will be printed

