# Format specifier are used to format a value on the basis of the flags that are inserted there.

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# print(f"Price I is {price1:.2f}")
# print(f"Price II is {price2:.1f}")
# print(f"Price III is {price3:.3f}")


# print(f"{price1:10}") #allocates a total of 10 character spaces for the variables
# print(f"{price2:010}")
# print(f"{price1:<10}") #left justify
# print(f"{price1:>10}") #right justify
#
# print(f"{price1:^15}")

price_car = 235325238525.09789676
print(f"{price_car:,.3f}")