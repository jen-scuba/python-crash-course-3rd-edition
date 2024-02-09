motorcycles = ['honda xl70', 'kawasaki kd125','yamaha radian', 'ducati monster', 'bmw r1250r']

print(f"I have owned many motorcycles - here is a list of a few")
for i in range(len(motorcycles)):
    print(motorcycles[i])

current_motorcycle = motorcycles.pop()
print(f"\n{current_motorcycle} is my current motorcycle!")