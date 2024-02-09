# Chapter 7 - User Input and While Loops
# Try it yourself7-4_movie_ticket.py


prompt = "\nTo determine the price of you movie ticket, please enter your age : "

while True:
    age = input(prompt)
    age = int(age)

    if age <= 3:
        print(f"Because you are {age} years old, you ticket is free!")
        break
    elif age >= 3 and age < 12:
        print(f"Because you are {age} years old, you ticket is $10.00.")
        break
    elif age > 12:
        print(f"Because you are {age} years old, you ticket is $15.00.")
        break