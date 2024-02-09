# Chapter 7 - User Inpt and While Loops
# parrot.py


# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# add a while loop
prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)