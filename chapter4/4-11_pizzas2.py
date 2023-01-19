pizza_types = ["Margarita", "Quatro Stazione", "Quatro Fromagi", "Pepperoni"]

friend_pizzas = pizza_types[:]

pizza_types.append("Marinara")
friend_pizzas.append("Tuna")

print("\nMy favourite pizzas are:")
for pizza in pizza_types:
    print(pizza)

print("\nMy friends favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

    

