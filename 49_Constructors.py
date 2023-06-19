# A constructor is a special type of member function that is called automatically when an object is created
# They help in creating an object, helps in initialization
# There are in general two types of constructor; default and parameterized 

# Tha min purpose of the constructor is to initialize values

# PS: Constructor returns "None", returns nothing
# Default constructor - no any arguments, has self arguments, that points to the obj that invokes it
class default:
    def __init__(self):
        print("This is default constructor without parameter")

def_obj = default()

# Parameterized constructor - takes arguments

class paramterized():
    def __init__(self, name, age):
        print("This is parameterized constructor with two parameters 'name' and 'age'")
        self.myName = name
        self.myAge = age

par_obj = paramterized("Nayan", 20)




class Cons:
    name= "Nayan"
    age = 20

    def Data(self):
        print(f"Name is {self.name} and age is {self.age}")

obj = Cons()
obj.Data()

# So how to make constructor? 

class Cons:
    def __init__(self): #a special keyword is used to define a constructor in Python which is __init__
        print("I am constructor and i am defined by a special keyword __init__")
    name= "Nayan"
    age = 20

    def Data(self):
        print(f"Name is {self.name} and age is {self.age}")

obj = Cons() # now creating an obj will automatically invoke the constructor, will be automatically called, and the contents of the constructor will be executed

# we can even pass parameter to the constructor and change the values

class Mat:
    def __init__(self, a, b): #constructor taking two parameter a, and b
        print("Hey this is constructor called by obj")
        self.length = a #stting the value of length as a and breadth as b
        self.breadth = b
    def area(self):
        print(f"The value of length is {self.length} and the value of the breadth is {self.breadth}")

obj1 = Mat(10,5) #creating obj, constructor gets automatically invoked for obj1 with two arguments 10 and 5
obj2 = Mat(20,10) #creating obj2, constructor gets automatically invoked for obj2 with two arguments 20 and 20
obj1.area()
obj2.area() 


# So yeah this much for today! Today we talked about