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

# finding certain elements in the list - we can find the presence of certain elements inside a list by using a if condition : 
if 10 in lis:
    print("True")
else:
    print("False") # the output will be false as 10 is not inside the list

# List slicing : List slicing is as same as string slicing

print(lis[1:5]) # [2,3,4,5] will be the output 

# PS : If you dont know the slicing operations and the way to do slicing, please refer to past session where i have talked about slicing in very details.



# List comphrehension : This is the process of making a new list

lis2 = [k for k in range(10)]
print(lis2) # it will make a new list, where K is a random variable, and then for loop is started till the range of 10, so it will give a output of :
# [0,1,2,3,4,5,6,7,8,9], 10 will not be printed as it will range-1

# But what if we want to print 1 to 10
# we can just increment the value of random variable by 1, Eg : 

new = [a+1 for a in range(10)]
print(new) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

li3 = [k for k in range(50) if k%5==0]
print(li3)

# So range has been decided as 50 and a conditon is given if k modulus 5 == 0 (multiples of 5), then print it
# so the output will be [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
