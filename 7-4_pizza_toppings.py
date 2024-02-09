# Chapter 7 - User Input and While Loops
# Try it yourself 7-4_pizza_toppings.py

# add a flag
prompt = "\nPlease enter the toppings you would like on your pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    toppings = input(prompt)

    if toppings == "quit":
        active = False
    else:
        print(toppings)
