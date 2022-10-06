# 9.4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, new_customers):
        self.number_served += new_customers

restaurant = Restaurant("ratatouille", "french")

# Without methods
print("Current value: ", restaurant.number_served)
restaurant.number_served = 10
print("New value: ", restaurant.number_served)

# With setter method
print("\nWith setter method")
print("Current value: ", restaurant.number_served)
restaurant.set_number_served(7)
print("New value: ", restaurant.number_served)

# With increment method
print("\nWith increment method")
print("Current value: ", restaurant.number_served)
restaurant.increment_number_served(2)
print("New value: ", restaurant.number_served)
