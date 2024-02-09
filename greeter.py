# Chapter 7 - User Inpt and While Loops
# greeter.py

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# multi-line input()
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
