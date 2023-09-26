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
    
# Instance level variables - They are the variables of instances/objects