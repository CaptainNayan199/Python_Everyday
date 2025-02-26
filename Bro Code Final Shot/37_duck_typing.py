# duck typing = another way of achieving polymorphism besides inheritance
# If it looks like a duck, quack like a duck, it must be a duck.


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    alive = False
    def speak(self):
        print("Honk")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)