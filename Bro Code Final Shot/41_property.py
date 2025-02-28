# @property is a decorator that allows us to defne a method as a property(it can be accessed like an attribute), it gives us getter, setter, and deleter method

class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height
    @property
    def width(self):
        return self._width

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be getter than 0")

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be getter than 0")

    @height.deleter
    def height(self):
        del self._height
        print("The height has been deleted!")

    @width.deleter
    def width(self):
        del self._width
        print("The width has been deleted!")


rect = Rectangle(10,5)
# print(rect._height)
# print(rect._width)

rect.height = 20
rect.width = 10

del rect.height
del rect.width






