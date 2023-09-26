# Variables can be classified as instance and class level in python. They can be defined in class level and at the instance level
# So what are they? How to understand them ?

# Class variables : They are those types of variables that are defined at the class level and are shared among all the instances of the class. Every instances of that class can enjoy that variables. Let's see with an example : 

class Myclass:
    total = 40 #so this all variables are class level variables
    name = "Nayan"
    age = 22
    def __init__(self):
        print(f"My name is {self.name} and i am {self.age} years old and there are {self.total} students in my class")
        
obj = Myclass()
obj2 = Myclass()   #all the instances of the class Myclass can access those calss level variables
    
# Instance level variables - They are the variables of instances/objects. Each instances or objects can have unique and different variables and their respective values accordingly
# Let's see with an example, i will modify the above example a bit to show it

class Myclass:
    # total = 40
    # name = "Nayan"
    # age = 22
    def __init__(self, total, name, age): #this total, name, and age are all instance level variables
        self.name = name
        self.total = total
        self.age = age
        print(f"My name is {self.name} and i am {self.age} years old and there are {self.total} students in my class")
        
obj = Myclass(40, "Nayan", 22) # see here these are the variables passed as an arguments
obj2 = Myclass(30, "Ujjwal", 20)

# Different instances can have different variables, depending upon the requirement.
# Just remember : Class variables are available for every instances of the class, but instance variables are also for instances but different instances can have different variables values.
# So yeah this is it all about class level variables and instance level variables in python. Tomorrow we will be looking at different methods of class
# Thank you! Happy coding !