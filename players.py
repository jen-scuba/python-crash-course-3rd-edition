players = ['charles','martina','michael','florence','eli']
print(players)

print(players[0:3])
print(players[:3])

print(players[:4])
print(players[2:])

# 4-10
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
print("\nHere are three players from the middle of the list")
for player in players[1:4]:
    print(player.title())

print("\nHere are the last three players from the middle of the list")
for player in players[-3:]:
    print(player.title())