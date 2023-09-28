# Today we are going to see about some important methods that are used mostly in python.
# We will be looking at dir(), __dict__, help() methods for today. Well __dict__ is attributes, not actually a methods. So let's see about them in detail.

# dir() methods - it is a built-in function in python that is used for object introspection(means looking what operation we can perform on objects). Dir() stands for directory as it lists all the essentials methods that can be performed under certain objects. It is used to list all the attributes and methods.

name = "Nayan"
print(dir(name))
# output -------> : ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# So these are all methods that can be performed on name variable with string value

name = "Nayan"
print(dir(name))

print(name.__len__())  # 5

# dict() attribute - In Python, the dict (dictionary) is a built-in data type used to store key-value pairs. A dictionary is a mutable, unordered collection of items where each item consists of a key and its associated value.
# This attribute converts the objects values into key value pairs

class Myclass:
  def myinfo(self, name, age, num):
    self.name = name
    self.age = age
    self.num = num

obj = Myclass()
obj.myinfo("Nayan", 22,98713)
print(obj.name)
print(obj.age)
print(obj.num)

# Now using dict()

print(obj.__dict__) # {'name': 'Nayan', 'age': 22, 'num': 98713}

# help() method - this method is used to get information about objects, classes, attributes, methods, and all the information about certain elements.

class Myclass:

  def __init__(self, name, age, num):
    self.name = name
    self.age = age
    self.num = num

  def myMethod(self):
    print("Hello I am a method of Myclass class")


obj = Myclass("Nayan", 22, 23523)

print(help(Myclass))

