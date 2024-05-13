def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

# The single astersik * before toppings caused python to create
#   a tuple called toppings of the 1 or more topping values provided


def make_pizza_1(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza_1("sausage", "pepperoni")
make_pizza_1("mushrooms", "green peppers", "onions", "extra cheese")


# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza woith th efollowing toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")