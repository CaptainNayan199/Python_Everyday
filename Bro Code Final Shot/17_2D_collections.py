# two dimensional list in python
from typing import get_origin

# fruits = ["Mango", "Apple", "Pineapple", "Guava"]
# vegetables = ["Potato", "Carrots", "Peas", "Spinach"]
# meats = ["Chicken", "Fish", "Mutton"]
#
# groceries = [fruits, vegetables, meats]
# # print(groceries[0][3])
#
# for gro in groceries:
#     for data in gro:
#         print(data, end = " ")

groceries = [["Mango", "Apple", "Pineapple", "Guava"],
             ["Potato", "Carrots", "Peas", "Spinach"],
             ["Chicken", "Fish", "Mutton"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()