# 10.11
import json

filename = "favorite_number.json"
with open(filename, "r") as f:
    favorite_number = json.load(f)
    print(f"I know your favorite number! It's {favorite_number}.")
