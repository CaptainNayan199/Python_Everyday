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

# 2  __str__(self): This method is called when you use the str() function or print() to represent an object as a string.
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass object with value: {self.value}"

obj = MyClass(42)
print(obj)  # Prints "MyClass object with value: 42"


# 3  __len__(self): This method lets you define the behavior of the len() function for objects of your class.

class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

my_list = MyList(["Nayan", "Ujjwal", "Neha", "Binita", "Chandra", "Siteee"])
length = len(my_list)   # Calls my_list.__len__() to get the length
print(length)

# These dunder/magic methods provide a way to customize the behavior of your custom objects, making your code more readable and intuitive when working with instances of your classes.
# So this is it. There are tons of dunders methods in python
