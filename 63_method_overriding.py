# Method overriding in python is a concept of oop where a subclass provides a specific implementation for a method that is already defined in its parent class. This allows the subclass to customize or extend the behavior of the inherited method while keeping the same method name.

# Let's see with an simple example : 

class Parent:
    def __init__(self):
        print("Ok from the parent class ")
    def Method(self):
        print("This is parent method and i will be over ridden by the child class.")


class Child(Parent):
    def __init__(self):
        print("Ok from the child class")
    def Method(self):
        print("This is child method")
    

# Now i have two classes, one is parent and the other one is child class.
# Both classes have a common method i.e Method(), but their content are different.
        
# Now let's make the object of child class and see how overridden works.

child = Method()
child.Method() #this will give 'This is child method' as an output. But why ? 
# It's because the child class has the same method name as parent name and hance it has overridden, coz the child method will get first priority.
# If there was no method with the name Method in child class