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
