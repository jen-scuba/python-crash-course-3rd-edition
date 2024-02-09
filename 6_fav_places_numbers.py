# 6-9 Favorite Places

favorite_places = {
    "jen": ["bonaire", "belize", "utila"],
    "jill": ["venice", "london"],
    "max": ["albuquerque"],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    else:
        print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

# 6-2 Favorite Numbers

fav_nums = {"george": 5, "mike": 79, "bob": 1, "chris": 3, "max": 1989}

for k, v in fav_nums.items():
    print(f"{k.title()}'s favorite number is {v}.")

print("\n")

# 6-10 Favorite Numbers II
favorite_numbers = {
    "george": [5, 21, 99],
    "mike": [79, 1, 12],
    "bob": [1, 2, 3],
    "chris": [23, 3, 86],
    "max": [1989],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name}'s favorite number is:")
    else:
        print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
