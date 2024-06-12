"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5
letters. Randomly select 4 numbers or letters from the list and print a message
saying that any ticket matching these 4 numbers or letters wins a prize.
"""

from random import choice

values = (
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    "a",
    "b",
    "c",
    "d",
    "e",
)

winning_match_set = []
for i in range(4):
    winning_match_set.append(choice(values))

print(
    f"Any ticket matching these 4 numbers or letters wins a prize: {winning_match_set}!"
)