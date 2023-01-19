class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        print("The restaurant is open.")
    def set_number_served(self, served_customers):
        self.number_served = served_customers
    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("Amazonico", "Asian Fusion")
restaurant.number_served = 10
restaurant.set_number_served(20)
restaurant.increment_number_served(30)

print(restaurant.number_served)

