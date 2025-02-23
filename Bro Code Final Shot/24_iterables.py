# iterables -> an object that can return its elements one at a time, allowing it to be iterated over in a loop

# num = [1,2,3,4,5]
# for i in num:
#     print(i)
# print()
# for y in reversed(num):
#     print(y)

# fruits = ("Mango", "Orange", "Banana", "Cherry", "Litchi")
# for fruit in fruits:
#     print(fruit, end="  ")

# cars = {"Lambo", "Bugatti", "Mercedes", "Ferari", "Volkswagen"}
# for car in cars:
#     print(car, end="    ")

# name = "Nayan Pathak"
# for na in name:
#     print(na, end="  ")

dicti = {"Name":"Nayan", "Age":22, "Address":"Birtamode", "isMarried": False}
for key in dicti.keys():
    print(f"{key}", end="  ")
print()
for value in dicti.values():
    print(f"{value}", end="  ")
print()
for a,b in dicti.items():
    print(f"{a} : {b}")

