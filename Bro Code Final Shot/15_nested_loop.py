# a loop inside a loop is known as nested loop

# outer loop:
#     inner loop

# for x in range(5):
#     for i in range(1,5):
#         print(i, end="")
#     print()


# rectangle printing

rows = int(input("Enter the number of rows : "))
cols = int(input("Enter the number of cols : "))
symbol = input("Enter a symbol to use : ")

for i in range(rows):
    for y in range(cols):
        print(symbol, end="")
    print()