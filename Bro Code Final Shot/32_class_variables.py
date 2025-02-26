# class variables = they are shared among all the instances of a class
# it is defined outside the constructor
# allows us to share the data among all the objects created from that class

class Student:
  
  class_year = 2025
  
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
  

std1 = Student("Nayan", 22)
std2 = Student("Sita", 22)


print(std1.name)
print(std2.name)
print(std1.class_year)