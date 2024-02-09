# Chapter 7 - User Input and While Loops
# parrot.py

# add a flag
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\n(Enter 'quit' to end the program.) "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)