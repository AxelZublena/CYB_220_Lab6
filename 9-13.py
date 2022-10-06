# 9.13
import random

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        value = random.randint(1, self.sides)
        print(f"The die rolled on {value}.")

die6 = Die()
die10 = Die(10)
die20 = Die(20)

dies = [die6, die10, die20]

for die in dies:
    print("\nNew die: ")
    for roll in range(10):
        die.roll_die()
