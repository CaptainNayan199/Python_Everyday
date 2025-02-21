# Concession stand program

menu = {"MO:MO": 120, "Pizza": 280, "Chowemin": 130, "Fry Rice": 200, "Thukpa": 60, "Samosa": 15}

cart = []
total = 0

print("---------------MENU----------------")
for key, value in menu.items():
    print(f"{key:10} : ${value}")
print("-------------------------------")

while True:
    food = input("Select an Item [q to quit]: ")
    if food.lower() == 'q':
        break
    else:
        cart.append(food)
        total = total + menu.get(food)
print(f"Your total is : ${total}")