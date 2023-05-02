
# Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop.
# it is used to keep record of number of iterations in loop
# enumerate function is a built in function in python that allows us to loop over a sequence anf get the index and value of each element in the sequence at the same time


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

# so in the above program we are explicityl telling the interpreter that

# SO yeah this much for today, we will meet tomorrow, we will talk about enumeration in python.
# Thank you! Happy coding.