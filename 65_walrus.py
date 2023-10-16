# Wlarus operator is a new thing in python. It came in practice after python 3.8 version. That means python version older than 3.8 does not support walrus operator. It is very useful operator in python.
# So this operator allows us to assign value to the variable within an expression.

# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

# Let's see with an example :
        
userId = [1,2,3,4,5,6,7,8,9,10]

while(i := len(userId)) > 0:
    print(userId.pop())




sample_data = [
	{"userId": 1, "name": "rahul", "completed": False},
	{"userId": 2, "name": "rohit", "completed": True},
	{"userId": 3, "name": "ram", "completed": False},
	{"userId": 4, "name": "ravan", "completed": True}
]

for i in sample_data:
    if (name:= i.get("name")) and (id := i.get("userId")) and (com:=i.get("completed")):
        print(f"The names in the list are : {name} and his userId is {id}. His state of assignment completion is {com}")
        
# So this is how walrus := operator can be very useful in python

# We can even use walrus operator to take user input and even inside of logical statement. For eg : 
nList = ["Nayan", "Ujjwal", "Birendra", "Hawamanxe", "Jarry"]

if(name:=input("Enter your name : ")) in nList: #See here i am asking for user input, and than storing that user input in name variable and then again checking for the existence of the value of that variable in the nameList.
    print("Your name is ", name)
else:
    print("Name not in the list.")
    
# If we want to do it without the use of wlarus operator than it becomes something like this : 


nList = ["Nayan", "Ujjwal", "Birendra", "Hawamanxe", "Jarry"]
name = input("Enter your name : ")
if name in nList:
    print("Your name is ", name)
else:
    print("Name not in the list.")

# Now lets see one more beautiful example : 

food_list = []
while True:
    fruit = input("What fruit do you like sir/madam ? : ")
    if fruit== ("quit" or "Quit"):
        break
    food_list.append(fruit)
print(f"Your favourite fruit are : {food_list}")
# A simple program where theres en empty list, and user are asked about their favourite foods and is entered into the list. No problem right ? Now let's rewrite this program by the use of walrus operator


food_list = [] #an empty list
while (fruit:=input("What fruit do you like sir/madam ? : ")) != "quit":
    food_list.append(fruit)
print(f"Your favourite fruit are : {food_list}")
# See the magic of walrus operator here, code is readable as well as the code is short too. The same thing can be done in way more shorter way by the use of walrus operator.

# So yeah this was all about python walrus operator. It's a very useful operator.
# Thank you!