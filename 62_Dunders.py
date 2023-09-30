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
# So this is it. There are tons of dunders methods in python but but but..
# Some of the popular and widely used dunder methods in python are : 

# # __init__: Constructor method, called when you create a new object.
# __str__: Called by the str() function and print() to represent an object as a string.
# __repr__: Used to represent an object as a string for debugging purposes.
# __len__: Defines the behavior of the len() function for objects of the class.
# __getitem__: Enables indexing like obj[key].
# __setitem__: Enables assignment via indexing like obj[key] = value.
# __delitem__: Enables item deletion using del obj[key].
# __iter__: Defines how objects are iterated over in a loop.
# __next__: Used in conjunction with __iter__ to define iteration behavior.
# __contains__: Allows you to use the in keyword to check for item existence.
# __eq__: Defines equality behavior (used with ==).
# __ne__: Defines non-equality behavior (used with !=).
# __lt__: Defines less-than behavior (used with <).
# __le__: Defines less-than-or-equal-to behavior (used with <=).
# __gt__: Defines greater-than behavior (used with >).
# __ge__: Defines greater-than-or-equal-to behavior (used with >=).
# __add__: Defines behavior for the + operator.
# __sub__: Defines behavior for the - operator.
# __mul__: Defines behavior for the * operator.
# __truediv__: Defines behavior for the / operator (true division).
# __floordiv__: Defines behavior for the // operator (floor division).
# __mod__: Defines behavior for the % operator (modulo).
# __pow__: Defines behavior for the ** operator (exponentiation).
# __abs__: Defines behavior for the abs() function.
# __call__: Allows an instance to be called as a function.
# __enter__ and __exit__: Used for context management with the with statement.
# __getattr__: Called when an attribute is accessed but not found.
# __setattr__: Called when an attribute is set.
# __delattr__: Called when an attribute is deleted.
# __hash__: Defines the object's hash value for use in hash-based collections.
# __instancecheck__ and __subclasscheck__: Used for type checking and isinstance/issubclass checks.

# Tomorrow we will be looking at the concept of method overriding (we have talked about that a bit previously btw) in details.
# Thank you! Happy coding !