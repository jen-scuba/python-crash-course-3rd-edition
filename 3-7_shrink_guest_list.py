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

print(f"\nSadly, I've just been informed that I can only invite 2 guests to dinner.\n")

# number_of_guests = len(guests)
# print(f"number_of_guests = {number_of_guests}")


for i in range(len(guests) - 2):
    name = guests.pop()
    print(f"{name.title()} my sincerest apologies, but I need to cancel your dinner invitation tonight.")

# number_of_guests = len(guests)
# print(f"number_of_guests = {number_of_guests}")   

for i in range(len(guests)):
    idx =- i
    print(f"\n{guests[idx].title()}, we're still on for dinner tonight at 8pm!.")
    del(guests[idx])

print(f"List of guests: {guests}")