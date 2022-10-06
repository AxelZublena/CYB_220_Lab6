# 9.15
import random

values = [18, 3892, 2, 3, 43, 342, 12, 123, 98, 19, "a", "b", "c", "d", "e"]

def calculate_winning_values(values):
    winning_values = []
    for counter in range(4):
        rand_index = random.randint(0, len(values)-1)
        winning_values.append(values[rand_index])

    return winning_values


my_ticket = ["a", "d", 12, 98]
counter = 0
while True:
    counter += 1
    if my_ticket == calculate_winning_values(values):
        break

print(f"The winning values {my_ticket} were found after {counter} draw.")
