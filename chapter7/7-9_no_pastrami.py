sandwhich_orders = ["BLT", "Pastrami", "Ham & Cheese", "Pastrami", "Tuna Mayo", "Chicken Salad", "Pastrami"]

print("The deli has run out of pastrami.")

while "Pastrami" in sandwhich_orders:
    sandwhich_orders.remove("Pastrami")

for sandwhich in sandwhich_orders:
    print(sandwhich)
