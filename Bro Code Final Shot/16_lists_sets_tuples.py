# list in python are used to store multiple variables inside a big bracket []. Ordered and mutable(changeable). Duplicate is allowed
# set in python are also used to store multiple variables inside a curly braces {}. Unordered and immutable, no duplicate data is allowed
# tuples are used to store multiple values inside a small braces (). Ordered and immutable. Duplicate data is allowed. Fastest

fruits = ["Mango", "Orange", "Banana", "Coconut"]
print(fruits)
print(fruits[0])
# print(fruits[1:4])
# print(fruits[-3:-1])
# print(fruits[::2])

for fruit in fruits:
    print(fruit, end = ",")

# methods for collections
# cars = ["Bugatti", "Ferari", "Mustang", "Thar"]
# # print(dir(cars))
# print(len(cars))
# print("Ferari" in cars) #checking whether the given item is in the list or not ?
# cars[0] = "Lambo"
# print(cars[0])
#
# cars = ["Bugatti", "Ferari", "Mustang", "Thar"]
# # cars.append("Ford") #add pineapple at the end of the list
# # cars.remove("Mustang")
# # cars.insert(0, "Nissan")
# # cars.sort()
# # cars.reverse()
# # cars.clear()
# # print(cars.index("Hahahahaha"))
# print(cars.count("Mustang"))
#
# print(cars)


# Sets

# fruits = {"Apple", "Mango", "Pineapple", "Guava", "Banana", "Jackfruit"}
# print(len(fruits))
# print("Beery" in fruits)
# fruits.add("Grapes")
# fruits.remove("Jackfruit")
# fruits.pop()
# fruits.clear()
# print(fruits)

# tuples

# fruits = ("Apple", "Mango", "Pineapple", "Guava", "Banana", "Jackfruit")
# # print(len(fruits))
# # print("Guava" in fruits)
# print(fruits.index("Mango"))
# print(fruits.count("Mango"))
# print(fruits)
#
# for fruit in fruits:
#     print(fruit)
