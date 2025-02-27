# static method belongs to a class rather than any object from that class(instance)
# generally used for utility function
# Instance methods is for operations on instances of the class
# static methods is for utility functions that do not need access to class data.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position} "

    @staticmethod
    def isvalid(position):
        valid_pos = ["Manager", "Cook", "Cashier", "Cleaner"]
        return position in valid_pos

print(Employee.isvalid("Manager"))

emp1 = Employee("Raj", "HOD")
print(emp1.get_info())
