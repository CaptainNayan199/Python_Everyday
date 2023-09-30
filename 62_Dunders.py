# So what are dunder methods? or what are magic methods ?
# We have been using them for so long period of time, but we dont know abt thems

# Dunder, or magic methods in Python, are special methods that start and end with double underscores (e.g., __init__, __str__, __add__). These methods have special meanings and are used to define how objects of a custom class behave in various situations.

# Let's see with some examples: 
# 1 __init__(self, ...): This method is called when you create a new object from a class. It initializes the object's attributes. It is an constructor, we all know about it.
class MyClass:
    def __init__(self, value):
        self.value = value
        print(self.value)

obj = MyClass(42)  # Initializes obj with a value of 42


