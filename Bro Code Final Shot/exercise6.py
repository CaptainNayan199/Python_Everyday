# creating a phone dial pad


first_row = [1, 2, 3]
second_row = [4, 5, 6]
third_row = [7, 8, 9]
last_row = ["*", 0, "#"]

dial_pad = [first_row, second_row, third_row, last_row]
# print(dial_pad)

for i in dial_pad:
    for x in i:
        print(x, end="  ")
    print()