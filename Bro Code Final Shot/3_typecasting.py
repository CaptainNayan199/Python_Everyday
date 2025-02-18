# typecasting is a process of converting a varible from one data type to another data type

name = "Name"
my_age = 22
gpa = 3.9
isMarried = False

print(type(name))


gpa = int(gpa)
print(gpa)

print(float(my_age))

print(str(my_age))

print(type((str(my_age) + str(my_age))))

print(str(my_age)+"0")

name = bool(name)
print(name) # if the string variable is empty then the bool will return false;