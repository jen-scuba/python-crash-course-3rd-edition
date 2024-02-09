# 6-4 -> 6-3 was already employing looping 
# 6-5 Rivers
rivers = {
    "nile": "egypt",
    "mississippi": "united states of america",
    "amazon": "brazil",
}

# loop to print a sentence for river and country
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()
# loop to print the name of each river
for river in sorted(rivers):
    print(river.title())

print()
# loop to print the name of each country
for river in rivers:
    country = rivers[river]
    print(country.title())

print()
# polling devs for favorite language
developers = ['jen','bill','phil','amy','mike']
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for dev in developers:
    if dev in favorite_languages.keys():
        print(f"{dev.title()}, thank you for taking the poll!")
    else:
        print(f"{dev.title()}, you are invited to take the favorite language poll!")
