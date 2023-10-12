# Method overriding in python is a concept of oop where a subclass provides a specific implementation for a method that is already defined in its parent class. This allows the subclass to customize or extend the behavior of the inherited method while keeping the same method name.

# Let's see with an simple example : 

class Parent:
    def __init__(self):
        print("Ok from the parent class ")
    def pMethod(self):
        print("This is parent method")
    def abc(self):
        print("Hello from parent class. ")


class Child(Parent):
    def __init__(self):
        print("Ok from the child class ")
    def cMethod(self):
        print("This is child method")
    def abc(self):
        print("Hello from child class.")

# Now i have two classes, one is parent and the other one is child class.
# Both classes have a common method i.e abc()
        