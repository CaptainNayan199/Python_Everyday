# inheritance allows a class to inherit attributes and methods from another class
# it helps with code reusability and extensibility

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True
    def eat(self):
        print(f"{self.name} is eating!")
    def sleep(self):
        print(f"{self.name} is asleep!")

class Dog(Animal):
    def speak(self):
        print("Dog is barking")

class Cat(Animal):
    def speak(self):
        print("Cat is Meowing")

dog = Dog("German Shepherd")
cat = Cat("Kitty")

print(dog.name)
print(dog.isAlive)
dog.eat()
dog.sleep()
dog.speak()
print()
print(cat.name)
print(cat.isAlive)
cat.eat()
cat.sleep()
cat.speak()