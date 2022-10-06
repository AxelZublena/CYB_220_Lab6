# 9.1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

restaurant = Restaurant("ratatouille", "french")

restaurant.describe_restaurant()
restaurant.open_restaurant()
