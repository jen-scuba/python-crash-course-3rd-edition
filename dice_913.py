"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number between 1
and the number of sides the die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint


class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initialize the die's attributes."""
        self.sides = sides

    def describe_die(self):
        """Print a statement describing the die size."""
        print(f"This die has {self.sides} sides.")

    def roll_die(self):
        """return a random number that represents a roll of the die."""
        rolled_die_number = randint(1, self.sides)
        return rolled_die_number


my_six_sided_die = Die()

print(f"Rolling the default die which has {my_six_sided_die.sides} sides.")
for x in range(10):
    roll = x + 1
    if roll == 1:
        print(f"{roll} roll of the die returns {my_six_sided_die.roll_die()}!")
    else:
        print(f"{roll} rolls of the die returns {my_six_sided_die.roll_die()}!")
print("\n\n")

my_ten_sided_die = Die(10)
my_20_sided_die = Die(20)

my_die = [my_ten_sided_die, my_20_sided_die]

for i in my_die:
    print(f"{i.describe_die()}")
    for x in range(10):
        roll = x + 1
        if roll == 1:
            print(f"{roll} roll of the die returns {i.roll_die()}!")
        else:
            print(f"{roll} rolls of the die returns {i.roll_die()}!")
    print("\n\n")