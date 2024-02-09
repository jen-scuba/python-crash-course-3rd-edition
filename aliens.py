# a list of three aliens (list of dictionaries)
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print()

#  use range to create a fleet of 30 aliens!
aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

print()
# change the first three aliens with the color green
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
        
# show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

# show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
