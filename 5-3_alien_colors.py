# 5-3 1
alien_color = "yellow"
print(f"Spoiler alert! The alien's color was {alien_color}")
if alien_color == "green":
    print("you just earned 5 points!")


alien_color = "green"
print(f"Spoiler alert! The alien's color was {alien_color}")
if alien_color == "green":
    print("you just earned 5 points!")

# 5-3 2
alien_color = "red"
print(f"Spoiler alert! The alien's color was {alien_color}")

if alien_color == "green":
    print("you just earned 5 points for shooting the alien!")

if alien_color != "green":
    print("you just earned 10 points!")

if alien_color == "green":
    print("you just earned 5 points for shooting the alien!")
else:
    print("you just earned 10 points!")

# 5-3 3
alien_color = "red"
print(f"Spoiler alert! The alien's color was {alien_color}")

if alien_color == "green":
    print("you just earned 5 points!")
elif alien_color == "yellow":
    print("you just earned 10 points!")
elif alien_color == "red":
    print("you just earned 15 points!")

if alien_color == "green":
    print("you just earned 5 points!")
if alien_color == "yellow":
    print("you just earned 10 points!")
if alien_color == "red":
    print("you just earned 15 points!")

if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
elif alien_color == "red":
    points = 15

print(f"you just earned {points} points!")
