# So today we will see about inheritance in python
# Inheritance is a very important topics in OOP.
# So what inheritance actually is ? ---> so inheritance is a key feature in OOP where a class can inherit methods, and properties of another class
# The same is in python as well, theres a parent class and we want to access its properties in another child class, to do so we need inheritance concepts.
# Code can be re used again and a relation ca be established within a class.

# A child class can access or inherit all the public and protected properties of the parent class

# There are several types of inheritance, some of them are single level, multi level, multiple, hybrid, hierarchial.


# Single inheritance : child class inherits single parent class
# Eg:

class Parent:
    def parent_method(self):
        print("Hello from parent class.")

class Child(Parent):
    def Child_method(self):
        print("Hello from Child class.")

obj = Child() #making child object

obj.Child_method() #accessing child methods with child objects.

obj.parent_method() #accessing parent method with child class.

# So this was about single inheritance.

# Multi level inheritance - Eg:

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
obj.children_method() #accessing 
obj.Child_method()
obj.parent_method()
