# class method allows operations on the class itself
# take cls as the first parameter, representing class itself

class Students:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count +=1
    # this is an instance method
    def get_info(self):
        return f"{self.name} : {self.gpa}"

    @classmethod
    def get_count(cls):
        return cls.count


std1 = Students("Nayan", 3.99)
std2 = Students("Sita", 4.0)
std3 = Students("Sitoshna", 4.0)


print(Students.get_count())
