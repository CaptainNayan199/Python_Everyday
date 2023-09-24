# So today we are going to see about static methods in python. What are they and what do they do ?
# Static methods can be directly called, no need to make an instance, even though they lie inside class.
# Let's see with an example : 

class Myclass:
    def myname(self):
        self.name = "Nayan"
    
    @staticmethod
    def opr(a, b): #no need to include self as an argument, because we are making an static method
        sum = a+b
        return sum

obj = Myclass()
obj.myname()
print(obj.name)

# Calling static methods
print(obj.opr(1,2)) # so we can call this this way or
print(Myclass.opr(1,2)) #this way as well

# So yeah this is it! It's simple, not very detailed, i hope the concept of static method is clear