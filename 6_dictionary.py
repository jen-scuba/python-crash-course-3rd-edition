#  6-1 Person

mom = {"first_name": "judy", "last_name": "kuenning", "age": "86", "city": "fairfax"}

for k, v in mom.items():
    print(f"key: {k} = {v.title()}")

print("\n")

# 6-2 Favorite Numbers

fav_nums = {"george": 5, "mike": 79, "bob": 1, "chris": 3, "max": 1989}

for k, v in fav_nums.items():
    print(f"{k.title()}'s favorite number is {v}.")

print("\n")

#  6-3 GLossary
glossary = {}
glossary["dictionary"] = "a collection of key value pairs"
glossary["variable"] = "a variable is a label that you can assign to values"
glossary["string"] = "a series of characters"
glossary["list"] = "a collection of items in a particular order"
glossary["conditional test"] = "a statement that tests true or false"

for k, v in glossary.items():
    print(f"{k.title()}:\n\t{v.capitalize()}.\n")
