# super() is a function used in a child class to call methods from a parent class(super class)
# and it allows us to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, isfilled):
        self.color = color
        self.isFilled = isfilled
    def test(self):
        print("Hey! I am from Parent class Shape")

class Circle(Shape):
    def __init__(self, radius, color, isfilled):
        super().__init__(color, isfilled)
        super().test()
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, length, breadth, color, isfilled):
        super().__init__(color, isfilled)
        super().test()
        self.length = length
        self.breadth = breadth

circle = Circle(4, "Red", True)
rect = Rectangle(10, 5, "Blue", False)

print(circle.color)
print(circle.isFilled)
print(circle.radius)
print(rect.isFilled, rect.color, rect.length, rect.breadth, end=" ")
