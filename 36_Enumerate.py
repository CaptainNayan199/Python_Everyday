
# Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop.
# it is used to keep record of number of iterations in loop
# enumerate function is 

temp = [30,33,34,36,38,40,46]
index = 0
for i in temp:
    print(i)
    if(index == 5):
        print("The temperature is 40")
        break
    index+=1
#so here i have a list of temperature, and when the index value is 5 i want it to print the temperature is 40, its kind of hectic, isn't is?

#so lets see how can we do this by the use of enumerate function in python

temp = [30,33,34,36,38,40,46]
for index, i in enumerate(temp):
    print(i)
    if(index == 5):
        print("The temperature is 40")
        break
    index+=1



my_name = "Nayan_Pathak"

for indexx, i in enumerate(my_name):
    print(indexx, i)  # same is the condition for string

# this methoda can be used for any data types like list tuples, and etc.


data = {"Nayan", "Ujjwal", "BIkas", "Santosh", "Tika"}

for indexx, i in enumerate(data):
    print(indexx, i) # same is the condition for set as well

# changing the starting value of the enumerate function

temp = [30,33,34,36,38,40,46]
for index, i in enumerate(temp, start=1):
    print(i)
    if(index == 5):
        print("The temperature is ", i)
        break
    index+=1

# so in the above program we are explicityl telling the interpreter that start the indexing from 1, not from 0 but from the 1.

# so when the value of index will be 5, it will print the value at index 5, which is non other than 38

# so the indexing of the list will be - 1,2,3,4,5...., in place of 0,1,2,3,4,5....

# so the enumerate function is often used when there is a need to loop over a sequence and perform some actions with both the index and value 

fruits = {"Apple", "Mango", "Papaya", "Orange", "Guava", "Watermelon", "Jackfruit"}

for index, i in enumerate(fruits):
    print(index+100," : ", i) # this is the best example for enumerate function

# SO yeah this much for today, we will meet tomorrow, we will talk about Virtual Environment in python.
# Tomorrow will be one of the very important session, because we are going to talk about Virtual environment, creating virtual environment and so many things regarding virtual environment.
# Thank you! Happy coding.