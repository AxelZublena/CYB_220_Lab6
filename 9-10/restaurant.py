# 9.10
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
