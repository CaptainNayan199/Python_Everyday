#Loops are used for printing some sequence of codes for some n number of times.
# They are used to execute some lines of codes for multiple times
#For loop can iterate over a sequence of iterable objects in python

#Numbers and strings/characters cn be printed in different way using for loops in python

#Let's print numbers using For loop
#We have to use range to print numbers in python

# num = 10
# for i in range (num): # i is used as certain variable that is storing the values from 0 to provided number.
    # print(i) # the number from 0 to num-1 is printed
# but what if we want to print starting from 1 ?
#just change inside print

    # print(i+1) #starts printing from 1

# Likewise multiplication table can be also printed using for and range 

# number = int(input("Which number table do you want ? "))

# for i in range (0, 10):
#     print(number, " X " , (i+1), " = ", number*(i+1), "\n"  )
    

# Similaryl we can print charaters of a particular string using for loop as well

# name = "Nayan" #printing characters in normal string
# for i in name:
#     print(i)

# list = ["Pilot", "Driver", "Airplane", "Flight"] #
# for i in list: printing each value of list
#     print(i)

# list2 = {"Name":"Nayan",
#          "Surname":"Pathak", 
#          "Hobby":"Studying"}
# for j in list2.keys():
#     print(j) #printing each keys in provided dict
# print("\n")
# for i in list2.values():
#     print(i) #printing the corresponding values of dict

# list3 = ("Nayan", "Santosh", "Roshan", "Tika")
# for i in list3:
#     print(i) #printing each content of tuples


#Range function in python always takes 3 parameters

for i in range (1, 12, 3):
    print(i)
    
# the first parameter signifies the starting values of the range
# the second parameter signifies the last/ending value of the range which is (n-1) or in our case(12-1)
# the third parameter signifies the jumping value i.e to jump by how much value

# for example : the above code output will be :

# 1 4 7 10 : The starting value is 1 and ending value is 12-1 = 11, but as per third parameter it should jump by 3

# so at first it will print 1, and them jump by 3 and then print 4 and then again jump by 3 and print 7 and then again jump by 3 and print 10, hence beacuse of this reason 11 is not printed at the last.


#So yeah this much for today, PS: Practice more for loops in python as they are the most used loops in not only python but also in other programming language
# So in tomorrow class we will talk about while loop in python

