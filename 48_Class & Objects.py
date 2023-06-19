# As talked in previous session classes are blue prints of real world, and objects are instance of an class

# Creating a class in python : class can be created in python by the use of class keyword.

class Nayan:
    print("Heloo Nayan this is Me")
    name = "Nayan"
    sub = "Computer"
    hobby = "Playing Games"
# So this is my new class with the name Nayan,

# Now i need to make an object of this class

obj1 = Nayan() #making a new object with the name obj

obj.name #accessing class variable from the object


class Test:
    a = 20
    b = 30
    def sum (self,a,b):
        return a+b
    
obj1 = Test() #creating an object
obj.sum(2,5) #accessing class methods using object


class Info():
    name = "Nayan"
    age = 20
    addr = "Btm"
    def infoo(self):
        print(f"My name is {self.name}. My age is {self.age}. I live in {self.addr}")
    

obj = Info() #creating a new object of the class Info
obj.name = input(" Enter your name : " ) #setting the name properties from the user input
obj.age = int(input("Enter your age : "))
obj.addr = input("Enter your current address : ")
obj.infoo()

# Self is passed as parameter in the infoo method ! But why ?
# self parameter - 
