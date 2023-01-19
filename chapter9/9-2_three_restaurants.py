class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        print("The restaurant is open.")


my_restaurant = Restaurant("amazonico", "asian fusion")
your_restaurint = Restaurant("abadia", "portugues")
his_restaurant = Restaurant("aarde", "spanish")

my_restaurant.describe_restaurant()
your_restaurint.describe_restaurant()
his_restaurant.describe_restaurant()