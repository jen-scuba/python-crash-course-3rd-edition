# Chapter 7 - User Input and While Loops
# 7_counting.py

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)