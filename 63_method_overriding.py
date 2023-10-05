# Method overriding in python is a concept of oop where a subclass provides a specific implementation for a method that is already defined in its parent class. This allows the subclass to customize or extend the behavior of the inherited method while keeping the same method name.

# Let's see with an simple example : 

class Parent:
    def __init__(self):
        print("Ok")
    def pMethod(self):
        print("This is parent method")


class Child:
        
