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

# We can even use walrus operator to take user input and even inside of logical statement.
nList = ["Nayan", "Ujjwal", "Birendra", "Hawamanxe", "Jarry"]

if(name:=input("Enter your name : ")) in nList:
    print("Your name is ", name)
else:
    print("Name not in the list.")
    