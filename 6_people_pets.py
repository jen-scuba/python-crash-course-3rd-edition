# 6-7 People
mom = {
    "first_name": "judy",
    "last_name": "kuenning",
    "age": 86,
    "city": "fairfax",
}

jeff = {
    "first_name": "jeffery",
    "last_name": "whatever",
    "age": 42,
    "city": "rockville",
}

mike = {
    "first_name": "michael",
    "last_name": "kuenning",
    "age": 66,
    "city": "phoenix",
}

people = [mom, jeff, mike]

for person in people:
    print(person)

print()
# 6-8 Pets
pet_0 = {
    "name": "tipsey",
    "type": "dog",
    "human": "jen",
}
pet_1 = {
    "name": "bass",
    "type": "dog",
    "human": "jen",
}
pet_2 = {
    "name": "Cassidy",
    "type": "dog",
    "human": "mary",
}

pets = [
    pet_0,
    pet_1,
    pet_2,
]

for pet in pets:
    print(pet)