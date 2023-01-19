from random import randint

list = [1, 4, 6, 7, 3, 6, 8, 9, 2, 6, "A", "H", "W", "C", "K"]

print( "Any ticket matching these four numbers or letters wins a prize:")
print(f"\t{list[randint(0, len(list) - 1)]} {list[randint(0, len(list) - 1)]} {list[randint(0, len(list) - 1)]} {list[randint(0, len(list) - 1)]}")



