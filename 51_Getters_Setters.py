# A function that are used to set any values (return) for any function can be referred to as getters and setters

# Getters in python - It is used to access the value of an object properties. They are used to return the value of a specific property. They are defined using the @property decorator.

# In Python property()is a built-in function that creates and returns a property object. A property object has three methods, getter(), setter(), and delete()

# Python @property is one of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes in such a way so that the user of your class no need to make any change in their code. 


# So firstly lets talk about encapsulation -  Encapsulation means wrapping up things, making it private
# In python we can make a private variable by using double underscore __ for example


class Enc:
    __age = 20

obj = Enc()
print(obj.__age) # here i will get an error, coz i am trying to acces private variable which i cannot

# But

class Enc:
    age = 20

obj = Enc()
print(obj.age) #here i will not get any error coz i an accessing a normal public unprotected variable by the use of object 
# Thsi process works for functions inside class as wells
print(obj.age) #here i will not get any error coz i an accessing a normal public unprotected variable by the use of object 
# Thsi process works for function inside class sxas well


# if we want to encapsulated variable than we can do by the use of methods or constructor

class Myclass:
    __name = "Nayan"
    __age = 20
    def __init__ (self):
        print(f"My name is {self.__name} and i am {self.__age} years old.")
        
obj = Myclass() # we can access this way only


class Myclass:
    __name = "Nayan"
    __age = 20
    def __init__ (self):
        print(f"My name is {self.__name} and i am {self.__age} years old.")
    def my_info(self, cllg):
        self.cllg_name = cllg
        print(f"My name is {self.__name} and i am {self.__age} years old and i am currently reading in {self.cllg_name} college.")
        
obj = Myclass()
obj.my_info("MMC") # like this way we can access 



class Myclass:
    __name = "Nayan"
    __age = 20
    def __init__ (self):
        print(f"My name is {self.__name} and i am {self.__age} years old.")
    def my_info(self, cllg):
        self.cllg_name = cllg
        print(f"My name is {self.__name} and i am {self.__age} years old and i am currently reading in {self.cllg_name} college.")

obj = Myclass()
print(obj.__name) # but we cannot access the variables like this
