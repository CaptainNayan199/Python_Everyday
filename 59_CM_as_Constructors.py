# In previous session we talked about class methods - they are those types of methods that belongs/bounds to the class itself rather than to the instances of the class.
# One of the most prominent use of class method in python is as aditional constructors. 
# We can set the values of the constructors using the class methods
# Think of a class methods as a way to create class objects in a different way.

# Using class methods as additional constructors can make your code more flexible and user-friendly, allowing you to create objects from a class in various ways depending on your specific needs.



class People:

  def __init__(self, name, age):  #constructor
    self.name = name
    self.age = age

  @classmethod
  def birthYear(cls, name, birthYear):
    agee = cls.findAge(birthYear)  #calling the static method
    return cls(name, agee) #invoking the class constructor with two parameters

  @staticmethod
  def findAge(birthYear):
    current_year = 2023
    age = current_year - birthYear
    return age


# Creating an object by default way
People1 = People("Nayan", 21)
print(f"My name is {People1.name} and my age is {People1.age}")

# Now lets use class method
People2 = People.birthYear("Ujjwal", 2002)
print(f"My name is {People2.name} and my age is {People2.age}")

# So yeah this is it. Today we learned how we can use classmethods as aditional constructor as well.
# Tomorrow 
