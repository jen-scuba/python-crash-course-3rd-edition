import sys

buffet = (
    "macaroni and cheese",
    "salad",
    "chicken pot pie",
    "beef stroganoff",
    "apple pie",
)

print("The food available in today's buffet are:")
for food in buffet:
    print(food.title())

try:
    buffet[-1] = ("cheese cake",)
except:  # catch *all* exceptions
    e = sys.exc_info()[0]
    print("\nError: %s." % e)
    
print("\nMoving on from error.")

buffet = (
    "mashed potatoes and gravy",
    "salad",
    "fried chicken",
    "beef stroganoff",
    "apple pie",
)

print("\nThe update menu items available in today's buffet are:")
for food in buffet:
    print(food.title())
