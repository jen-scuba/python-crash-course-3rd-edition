pizzas = ['four-cheese','everything', 'pepperoni']
for pizza in pizzas:
    print(f"{pizza.title()} is one of my favorite pizzas!\n")

print("Pizzas is my most favorite meal!")

friend_pizzas = pizzas[:]

pizzas.append("quattro-formaggio")
friend_pizzas.append("meat lovers")

print("\nMy favorite pizzas are:")
print(pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)
