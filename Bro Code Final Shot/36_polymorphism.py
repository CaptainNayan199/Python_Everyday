# polymorphism means to have more than one form
# can be achieved using inheritance or duck typing

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 1/2 * self.base * self.height


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping



shapes = [Circle(30), Triangle(10, 5), Pizza("Cheese", 10)]
for shape in shapes:
    print(f"{shape.area():.2f}cm²")