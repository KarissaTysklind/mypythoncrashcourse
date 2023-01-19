animals = ["cat", "tiger", "lion", "linx", "leopard", "cheetah"]

print("The first three animals in the list are:")
for animal in animals[:3]:
    print(animal.title())

print("The animals from the middle in the list are:")
for animal in animals[2:4]:
    print(animal.title())

print("The last three animals from the list are:")
for animal in animals[-3:]:
    print(animal.title())