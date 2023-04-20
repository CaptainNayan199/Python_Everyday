# In previous session we talked about sets, and today we are going to see about some important sets methods.
#they work in same ways as sets in mathematics.

set1 = {1,2,3,4,5}
set2 = {5,6,7,8}
print(set1+set2) # this is not the way to perform set operations
# well lets see some of the operations that can be performed in the set like union, intersection, etc.
print(set1.union(set2)) #this gives the union of two sets.

print(set1.intersection(set2)) #this gives intersection of two sets.

(set1.update(set2)) # this method is saying that update the value of set1 i.e put every unique values of set2 in set1. SO our output will be: 1,2,3,4,5,6,7,8
print(set1)
