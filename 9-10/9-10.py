# 9-10
from restaurant import Restaurant

restaurant = Restaurant("ratatouille", "french")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Setter method
print("\nSetter method")
print("Current value: ", restaurant.number_served)
restaurant.set_number_served(7)
print("New value: ", restaurant.number_served)

# Increment method
print("\nIncrement method")
print("Current value: ", restaurant.number_served)
restaurant.increment_number_served(2)
print("New value: ", restaurant.number_served)
