class Car:
    def __init__(self, name, color, for_sale):
        self.name = name
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("You are driving the car")

    def stop(self):
        print("You are stopping the car!")