# 4-3 Counting to 20
for num in range(1,21):
    print(num)
    
print()

# 4-4 One Million
# for num in range(1,1000001):
#     print(num)

# 4-5 Summing a Million
million = list(range(1,1000001))
print(min(million))
print(max(million))
print(sum(million))

print()
# 4-6 odd number list 
odd_numbers = list(range(1,20,3))
for num in odd_numbers:
    print(num)
    
print()
# 4-7 Threes
threes = list(range(3,30,3))
for three in threes:
    print(three)

print()
# 4-8 Cubes
cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)

print(cubes)
    
print()
# 4-9 Cubes using list comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)
