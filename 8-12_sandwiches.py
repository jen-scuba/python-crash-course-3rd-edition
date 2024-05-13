"""
8-12. Sandwiches: Write a function that accepts
a list of items a person wants on a sandwich. The
function should have one parameter that collects as
many items as the function call provides, and it
should print a summary of the sandwich that’s being
ordered. Call the function three times, using a
different number of arguments each time.
"""


def make_sandwich(*toppings):
    print(f"\nMaking sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich("chicken breast", "mayo", "cheddar cheese")
make_sandwich("roast beef", "swiss cheese", "mayo", "horse-raddish")
make_sandwich("grilled cheese")