# 9.2
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

restaurant1 = Restaurant("ratatouille", "french")
restaurant2 = Restaurant("alfredo", "italian")
restaurant3 = Restaurant("country road", "american")

restaurants = [restaurant1, restaurant2, restaurant3]

for restaurant in restaurants:
    print("\n")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
