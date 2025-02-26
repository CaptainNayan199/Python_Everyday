# multiple inheritance allows a class to inherit more than one class
# multilevel inheritance allows a class to inherit from another class that is already inheriting the other class :
# Eg - B class is inheriting A - B(A) , and the B is being inherited by C class - C(B)

# Multiple
# class A:
#     def my_methodA(self):
#         print("I am from A class")
#
# class B:
#     def my_methodB(self):
#         print("I am from B class")
#
# class C(A, B):
#     pass
#
# # class D:
# #     pass
#
# class_c = C()
# class_c.my_methodA()
# class_c.my_methodB()

# multi level inheritance

class A:
    def my_methodA(self):
        print("I am from A class")

class B(A):
    def my_methodB(self):
        print("I am from B class")

class C(B):
    def my_methodC(self):
        print("I am from C class")

class D(C):
    pass

class_d = D()
class_d.my_methodA()
class_d.my_methodB()
class_d.my_methodC()
