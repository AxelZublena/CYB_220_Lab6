# 9.6
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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self):
        print("Here are the available flavors of the ice cream stand: ")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")

ice_cream_stand = IceCreamStand("glacier", "ice cream", ["banana", "vanilla", "raspberry", "lemon"])
ice_cream_stand.display_flavors()
