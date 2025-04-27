# list comprehension is a concise way to create a lists in python.

import random

# doubles = []
# for x in range (1,11):
#     doubles.append(x*2)
# print(doubles)

# doubles = [x*2 for x in range(1,11)]
# triples = [y*3 for y in range(1,11)]
# squares = [a*a for a in range(1,11)]
# print(doubles)
# print(triples)
# print(squares)

# fruits = ["mango", "apple", "banana", "cherry"]
# upper_case = [fruit.upper() for fruit in fruits]
# print(upper_case)

# numbers = [1,-2,-6,3,6,-9]
# positive = [num for num in numbers if num >= 0]
# print(positive)

# numbers = [1,-2,-6,3,6,-9]
# neg = [num for num in numbers if num <= 0]
# print(neg)

# numbers = [1,-2,-6,3,6,-9,8,11,-7]
# even = [num for num in numbers if num%2== 0]
# print(even)

# numbers = [1,-2,-6,3,6,-9,8,11,-7]
# odd = [num for num in numbers if num%2== 1]
# print(odd)

grades = [random.randint(20,100), random.randint(20,100), random.randint(20,100), random.randint(20,100), random.randint(20,100), random.randint(20,100), random.randint(20,100)]
passed = [grade for grade in grades if grade>=60]
failed = [gr for gr in grades if gr<60]
print(passed, end="  ")
print(failed, end="  ")