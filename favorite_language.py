# polling devs for favorite language
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print()

for name in favorite_languages.keys():
    print(name.title())

print()

#  Same as above - it's the default behavior
for name in favorite_languages:
    print(name.title())

""" loop through the names in the dictionary as we did previously, 
    but when the name matches one of our friends, we’ll display a message 
    about their favorite language """

print()
friends = ["sarah", "phil"]

for name in favorite_languages:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language.title()}!")

# use the keys() method to find out if a particular person was polled
print()

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

# loop with key sort
print()

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print()
# loop for values only
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print()
# loop values wrapped in set to eliminate duplicates
print("The following languages have been mentioned wrapped in set():")
for language in set(favorite_languages.values()):
    print(language.title())
