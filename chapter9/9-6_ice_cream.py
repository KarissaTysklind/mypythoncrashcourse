class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        print("The restaurant is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["chocolate", "vanilla", "cream", "coffe", "cookies & cream"]
    def display_flavours(self):
        print(f"These are the flavours we have available:")
        for flavour in self.flavours:
            print(f"\t-{flavour}")

mrwhippy = IceCreamStand("Mr Whippy", "Ice Creams")
mrwhippy.display_flavours()