# super() is a function used in a child class to call methods from a parent class(super class)
# and it allows us to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, isfilled):
        self.color = color
        self.isFilled = isfilled
    def test(self):
        # print(f"My color is {self.color} and I am {'filled.' if self.isFilled else 'not filled.'}")
        return f"My color is {self.color} and I am {'filled.' if self.isFilled else 'not filled.'}"

class Circle(Shape):
    def __init__(self, radius, color, isfilled):
        super().__init__(color, isfilled)
        self.radius = radius
    def test(self): #method overriding!
        print(f"I am Circle! {super().test()}")

class Rectangle(Shape):
    def __init__(self, length, breadth, color, isfilled):
        super().__init__(color, isfilled)
        self.length = length
        self.breadth = breadth
    def test(self): #method overriding!
        print(f"I am Rectangle! {super().test()} ")

circle = Circle(4, "Red", True)
rect = Rectangle(10, 5, "Blue", False)

# print(circle.color)
# print(circle.isFilled)
# print(circle.radius)
# print(rect.isFilled, rect.color, rect.length, rect.breadth, end=" ")

circle.test()
rect.test()
