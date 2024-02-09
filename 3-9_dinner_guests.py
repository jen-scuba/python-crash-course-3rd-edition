guests = ['mom','dad','grandma norris', 'grandma ralston', 
          'grandpa ralston', 'grandpa Norris','grandpa kuenning']

for i in range(len(guests)):
    print(f"{guests[i].title()}, you are coordially invited to dinner tonight, December 8, 2023, at 8pm EST")


print(f"\n{guests[1].title()} can't make it.\n")
guests[1] = 'uncle roy'

for i in range(len(guests)):
    print(f"{guests[i].title()}, you are coordially invited to dinner tonight, December 8, 2023, at 8pm EST")

print(f"\nFound a bigger table!!!\n")

guests.insert((len(guests) + 1), 'aunt betty')
guests.insert((len(guests) + 1), 'aunt jackie')
guests.append('aunt joanne')

for i in range(len(guests)):
    print(f"{guests[i].title()}, you are coordially invited to dinner tonight, December 8, 2023, at 8pm EST")

print("\nTotal guests:", len(guests))
      