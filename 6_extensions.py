# 6-12
pizzas = {
    "meat-lovers": {
        "toppings": ["pepperoni", "sausage", "ham", "cheese"],
        "crust": "hand-tossed",
    },
    "three-cheese": {
        "toppings": ["asiago", "mozzarella", "parmesan"],
        "crust": "hand-tossed",
    },
    "supreme": {
        "toppings": ["pepperoni", "sausage", "green-pepper", "onion", "cheese"],
        "crust": "thin",
    },
}

# version 1 - unhappy with it....
for name, ingredients in pizzas.items():
    print(f"{name.title()} includes the following:")
    for toppings, crust in ingredients.items():
        print(f"\t{toppings}")
        print(f"\t{crust}")

print()

# version 2
for name, ingredients in pizzas.items():
    crust = ingredients["crust"]
    print(
        f"The {name.title()} pizza has a {crust.title()} crust with the following toppings:"
    )
    toppings = ingredients["toppings"]
    for topping in toppings:
        print(f"\t{topping}")
