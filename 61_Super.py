# In Python, the super() keyword is used to call methods or access attributes from a parent or superclass within a subclass. It allows you to inherit and reuse code from the parent class. 

class Parent:
  def pMethod(self):
    print("I am parent method")

class Child(Parent):
  def cMethod(self):
    print("I am child method")
    Parent().pMethod() #this method also can access the parent method
    self.pMethod() #this method can also access the parent method


child_obj  = Child()
child_obj.cMethod()
