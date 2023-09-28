# In Python, the super() keyword is used to call methods or access attributes from a parent or superclass within a subclass. It allows you to inherit and reuse code from the parent class. 

class Parent:
  name = "Nayan"
  def pMethod(self):
    print("I am parent method")

class Child(Parent):
  def cMethod(self):
    print("I am child method")
    Parent().pMethod() #this method also can access the parent method
    self.pMethod() #this method can also access the parent method
    print(self.name) #this method can access the attributes of the parent class.
    print(Parent().name) #this method can access the attributes of the parent class.

child_obj  = Child()
child_obj.cMethod()


# But we can do same thing from the use of super() method as well. Let's see it : 

class Parent:
  name = "Nayan"
  def pMethod(self):
    print("I am parent method")

class Child(Parent):
  def cMethod(self):
    print("I am child method")
    # Parent().pMethod()
    # self.pMethod()
    # print(self.name)
    # print(Parent().name)
    super().pMethod() #this can access the parent method
    print(super().name) #this can access the parent attributes, ezpz


child_obj  = Child()
child_obj.cMethod()

# Let's see an interesting thing: i.e overriding 

class Parent:

  def pMethod(self):
    print("I am parent method")


class Child(Parent):

  def cMethod(self):
    print("I am child method")
    super().pMethod()

  #suppose here i have another method that is same as parent method
  def pMethod(self):
    print("Heyyyyy")


child_obj = Child()
child_obj.cMethod()
child_obj.pMethod() #this will print Heyyyyy, coz it has its own pMethod


# But what if child class didnt have pmethod() ? 

class Parent:

  def pMethod(self):
    print("I am parent method")


class Child(Parent):

  def cMethod(self):
    print("I am child method")
    super().pMethod()


child_obj = Child()
child_obj.cMethod()
child_obj.pMethod() #this will print "I am parent method" why ? because parent class doen not have its own pMethod(), so it inherits from the parent class.

# We can even access parent class constructor using the child class, how ? let's see it

class Parent:

  def __init__(self, name, age):  #this is parent class constructor
    self.name = name
    self.age = age
    print(
        f"Hey myself {self.name} here, i am {self.age} years old. I got this values from my sub class"
    )


class Child(Parent):

  def __init__(self, name, age, number):
    super().__init__(name, age)
    self.number = number
    print(f"My number is {self.number}. I got this value from child class")


child_object = Child("Nayan", 22, 58738)

