# Variables can be classified as instance and class level in python. They can be defined in class level and at the instance level
# So what are they? How to understand them ?

# Class variables : They are those types of variables that are defined at the class level and are shared among all the instances of the class. Every instances of that class can enjoy that variables. Let's see with an example : 

class Myclass:
    Student = 40
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"My name is {self.name} and i am {self.age} years old.")
    
