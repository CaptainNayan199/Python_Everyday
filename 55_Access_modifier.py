# Today we are going to see about access modifie. So what are access modifiers?
# As name says, they are used to set the accessibility  or visibility of any variables, objects, methods, etc.
# There are 3 types of access modifiers in python. They are public which is the default one, private, and protected.
# These access modifiers provide restrictions on the access of member variables and methods of the class from any object outside the class.
# Private properties cannot be accessed outside of class, protected works within class.


# Imp - There is no private like thing in python, however naming variable or method by using dunder (double underscore ) is consider a good practice for private access, however it can be accessed in some ways. Let's see with an example.

# Let's see with an example 

class Nayan:
    def myname(self):
        # self.__name = "Nayan"
        self.name = "Nayan"

obj = Nayan()
obj.myname()
print(obj.name) #so it's simple, no any issue, just prints the attribute value

# But now let's make the attribute of the method private by using dunder and try accessing it.


class Nayan:
    def myname(self):
       self.__name = "Nayan"
       
obj = Nayan()
obj.myname()
print(obj.__name) #now this will give error, as we cannot directly access the private attributes of a class.
# But it can be accessed in indirect ways

class Nayan:
    def myname(self):
        self.__name = "Nayan"
        

obj = Nayan()
obj.myname()
print(obj._Nayan__name) #So this is called as name-mangling approach in python, typically this is not consider good practice but yeah knowing it might be a good work as well.

# In Python, when you prefix an instance variable with a double underscore like __name, Python performs name mangling to make it more difficult to accidentally override the attribute in subclasses. Name mangling adds a prefix to the variable name, based on the class name, to make it unique.