# 9-15 Lottery Analysis
"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind
of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that
keeps pulling numbers until your ticket wins. Print a message reporting how many times
the loop had to run to give you a winning ticket.
# """

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

my_ticket = [0, 5, "e", "b"]

attempts = 0
not_found = True

while not_found:
    attempts += 1
    winning_match_set = []
    for i in range(4):
        winning_match_set.append(choice(values))

    res = True
    for x in range(0, len(winning_match_set)):
        if (winning_match_set[x] != my_ticket[x]):
            res = False
            break
    print(f"random four selected {winning_match_set}")
    print(f"my ticket numbers {my_ticket}")

    if res:
        print(
            f"I have the winning ticket! {winning_match_set} " 
            f"in {attempts} trys!\n"
        )
        not_found = False
    else:
        print(f"attempt number {attempts}.\n")


# # Python3 code to demonstrate working of
# # Check if tuple and list are identical
# # Using loop
 
# # Initializing list and tuple
# my_ticket = [0, 5, "e", "b"]
# test_tup = (0, 5, "e", "b")

# # printing original list and tuple 
# print("The original list is : " + str(my_ticket))
# print("The original tuple is : " + str(test_tup))
 
# res = True
# for i in range(0, len(my_ticket)):
#     if(my_ticket[i] != test_tup[i]):
#         res = False
#         break

# # printing result
# print("Are tuple and list identical ? : " + str(res))
