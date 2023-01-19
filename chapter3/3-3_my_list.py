desserts = ["cake", "cupcake", "bread", "cake-pops", "croissants", "pie"]
flavours = ["chocolate", "strawberry", "bananna", "vanilla", "apple"]
print("I would like to eat some {flavour} {dessert}".format(flavour = flavours[0], dessert = desserts[0]))
print("I would like to make some {} {}s tonight!".format(flavours[1], desserts[1]))
print("I don't really like {} {}".format(flavours[2], desserts[2])
)
print("My favourite {dessert} is {flavour} {dessert}!".format(dessert=desserts[-1], flavour=flavours[-1]))