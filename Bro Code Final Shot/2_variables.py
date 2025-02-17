from psutil import disk_io_counters

# variables are a container that hold any kind of values either string, integer, boolean or any other kinds.

# String variables
first_name = "Nayan"
last_name = "Pathak"
fav_food = "Dumpling"
mail_address = "nayan@python.com"

print(first_name, last_name)

# using fstring - format string
print(f"Hello {first_name}! You like {fav_food}. Your email is {mail_address}")


# Integers variables
age = 22
quantity = 24
class_students = 32
print(f"You are {age} years old. And you are buying {quantity} items. And your class has {class_students} students")


# Float Variables
price = 3456.7
discount = 9.99
gpa = 3.78
print(f"The price is {price} and the discount on that is {discount}")
print(f"You have got {gpa} GPA")

# Booleans variables

isMarried = False
isStudent = True
isOld = False
isOnline = True

print(f"Are you a student ? : {isStudent}\nAre you married ? : {isMarried}")
if isMarried:
    print("The person is married")
else:
    print("The person isn't married")

if isOnline:
    print("The user is online")
else:
    print("The user isn't online")


usr_name = "Captain Nayan"
user_id = 14
isPlaying = False
age = 22.5





