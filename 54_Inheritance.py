# So today we will see about inheritance in python
# Inheritance is a very important topics in OOP.
# So what inheritance actually is ? ---> so inheritance is a key feature in OOP where a class can inherit methods, and properties of another class
# The same is in python as well, theres a parent class and we want to access its properties in another child class, to do so we need inheritance concepts.
# Code can be re used again and a relation ca be established within a class.

# A child class can access or inherit all the public and protected properties of the parent class

# There are several types of inheritance, some of them are single level, multi level, multiple, hybrid, hierarchial.

# The class that needs to be inheritated should be placed inside a parenthesis.


# Single inheritance : child class inherits single parent class
# Eg:

class Parent:
    def parent_method(self):
        print("Hello from parent class.")

class Child(Parent): #child class in inheriting parent class.
    def Child_method(self):
        print("Hello from Child class.")

obj = Child() #making child object

obj.Child_method() #accessing child methods with child objects.

obj.parent_method() #accessing parent method with child class.

# So this was about single inheritance.

# Multi level inheritance - It is a type of inheritance where A class is being inherited by B class and again B class is being inherited by C class.

class Parent:
    def parent_method(self):
        print("Hello from parent class.") 
        
class Child(Parent):
    def Child_method(self):
        print("Hello from Child class.")

class Children(Child):
    def children_method(self):
        print("Hello from Children class")

obj = Children() #creating  3rd class object
obj.children_method() #accessing 3rd class method with 3rd class object
obj.Child_method() # accessing child class method with 3rd class object
obj.parent_method() #accessing parent class method with 3rd class object.


# Multiple inheritance - It is a type of inheritance where class C is inheriting Both class A and B, a single class can inherit multiple(more than 2) class at the same time, the class to be inheritated needs to be placed inside a parenthesis seperated by comma.

# Eg:

class A:
    def from_a(self):
        print("Hello from class A")

class B:
    def from_b(self):
        print("Hello from child B")
        
class D:
    def from_d(self):
        print("Hello from child D")


class C(A, B, D): #class c is inheriting A, B and D class at the same time.
    def from_c(self):
        print("Hello from child C")
        
OBJ = C()
OBJ.from_a()
OBJ.from_b()
OBJ.from_c()
OBJ.from_d()

# So this was about multiple inheritance

# Another example of inheritance

class Teen: # this is our parent class.
    def __init__(self, name):
        self.name = name
        
    def showName(self):
        print("My name is "+self.name)
    
    def isMarried(self):
        return False
    
class Adult(Teen): #this is our child class and it is inheriting parent class Teen
    def isMarried(self):
        return True
        
object = Teen("Nayan") #creating an parent class object
object.showName()
print(f"My marrital status is {object.isMarried()}")

print("\n")

obj = Adult("Ujjwal") #creating an child class object, but for parent class as one arguments is being provided.
obj.showName()
print(f"My marrital status is {object.isMarried()}")


# Example 2:

class Sum:
    def __init__(self,a, b):
        self.a = a
        self.b  = b
    def sum(self):
        sum = self.a + self.b
        print("The sum is ", sum)
        
class Summ:
    def __init__(self,a, b,c):
        self.a = a
        self.b  = b
        self.c  = c
    def sum(self):
        sum = self.a + self.b + self.c
        print("The sum is ", sum)

class Child(Sum):
    def abc(self):
        print("I am from Child class")
        
class Childd(Summ):
    def abc(self):
        print("I am from Childd class")
        
object = Child(1,2)
object.sum()
object.abc()

object = Childd(1,2,3)
object.sum()
 

# Now providing value for parent class constructor from child class.
# we use - parent_class.__init__(arguments)

class Sum:
    def __init__(self,a, b):
        self.a = a
        self.b  = b

    def sum(self):
        sum = self.a + self.b
        print("The sum is ", sum)
        
class Child(Sum):

    def __init__(self, a, b, name):
        self.name = name

        Sum.__init__(self,a,b) #invoking parent class and providing arguments as well from the child class
        
    def Display(self):
        print("My name is ", self.name)

obj = Child(2, 3 ,"Nayan")
obj.Display()
obj.sum()



        

    
    