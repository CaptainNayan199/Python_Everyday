# shopping cart program exercise!

foods = []
prices = []
total = 0

while True:
    print()
    food = input("Enter a food to buy [press 'q' to quit] :  ")
    if food.upper() == "Q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food} as well : "))
        prices.append(price)
print("------------------Your Shopping cart--------------------")
for foo in foods:
    print(foo, end = "  ")
print()
for pri in prices:
    print(pri, end= "   ")
for price in prices:
    total += price
print(f"Your total is ${total}")