# examples of premanent list sorts
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

# examples of temporary list sort
cars = ['bmw','audi','toyota','subaru']
print("\nHere is the original list:")
print(cars)
      
print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# printing a List in reverse order - not to be confused with sort (alpha)
print("\nHere is the original list permanently ordered in reverse:")
cars.reverse()  # this is a permanent order change
print(cars)

# to put it back in the original order permanently - rinse and repeat
print("\nRinse and repeat to return to the list permanently in the original order:")
cars.reverse()  # this is a permanent order change
print(cars)

# Finding the length of a list
cars = ['bmw','audi','toyota','subaru']
print(len(cars))
