# 9.14
import random

values = [18, 3892, 2, 3, 43, 342, 12, 123, 98, 19, "a", "b", "c", "d", "e"]

winning_values = []
for counter in range(4):
    rand_index = random.randint(0, len(values)-1)
    winning_values.append(values[rand_index])

print(f"The ticket with the following values won: {winning_values}")
