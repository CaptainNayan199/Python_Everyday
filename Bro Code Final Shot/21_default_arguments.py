# default arguments : a default value for certain parameters
# default is used when that argument is omitted, makes program more flexible, reduces num of arguments
# 1. Positional     2. default      3. keyword      4. arbitrary


# def average(a,b=4,c=3):
#     return (a+b+c)/3

# # print(f"The average is {average(1,2,3)}")
# # # OR
# # print(f"The average is {average()}")
# # OR
# print(f"The average is {average(10):.2f} ")

import time

def count(end, start=0):
    for y in range(start, end+1):
        print(y)
        time.sleep(1)
    print("Done")

count(10)