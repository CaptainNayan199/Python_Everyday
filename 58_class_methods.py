# class methods are special kinds of methods that belongs to class itself, rather than to any instances of that class. It is a special kind of class function that is only work the class, not for the objects created from the class.
# They are defined inside a class, just like regular methods.
# The can be called outside a class, without need to define or create an object

# Why to create class methods ? 
# To modify class level variables

# How to create a class methods? - to create a class method in python we should use @classmethod as a decorator, and it should have the  class itself (usually named cls, or you can give any name) as its first argument. Here's a simple example:

class MyClass:
  class_variable = 10  # Class level variable
  myname = "Nayan"  #class level variable
  
  def __init__(self, value):
    self.instance_variable = value

  @classmethod
  def class_method(cls, x, name): #takes first argument as class
    cls.class_variable += x #updating the class variable value
    cls.myname = name #updating the myname values



# Create instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)


print(MyClass.class_variable)
print(MyClass.myname)

# Call the class method on the class itself
MyClass.class_method(5, "Ujjwal")

# Access class-level variables
print(MyClass.class_variable)  # Output: 5
print(MyClass.myname)

