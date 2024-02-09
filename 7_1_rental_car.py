# Chapter 7 - User Inpt and While Loops
#
# 7-1 rental_car
car = input("What kind of car would you like to rent today? ")
print(f"\nLet me see if I can find you a {car}.")

# 7-2 Restaurant seating
number = input("How many are in your party? ")
number = int(number)

if number > 8:
    print(f"\nYou'll have to wait for a table.")
else:
    print(f"\nYour table is ready.")

# 7-3 Multiples of Ten
number = input("Please provide a number. ")
number = int(number)

if number % 10 == 0:
    print(f"\nYour number is a multiple of 10!")
else:
    print(f"\nYour number is NOT a multiple of 10...")
