car = "suburu"
print("Is car == 'suburu'? I predict True.")
print(car == "suburu")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

car2 = "audi"
print("\nIs car == 'audi'? I predict True.")
print(car2 == "audi")

print("\nIs car == 'suburu'? I predict False.")
print(car2 == "suburu")

print("\nIs car or car2 a 'suburu'? I predict True")
print((car == "suburu") or (car2 == "suburu"))

print("\nIs car and car2 a 'suburu'? I predict False")
print((car == "suburu") and (car2 == "suburu"))

cars = ["suburu", "bmw", "audi", "ford"]
print("\nIs 'toyota' in cars? I predict false")
print("toyota" in cars)

print("\nIs 'toyota' NOT in cars? I predict True")
print("toyota" not in cars)

print("\nIs 'ford' in cars? I predict True")
print("ford" in cars)

print("\nIs 'audi' NOT in cars? I predict False")
print("audi" not in cars)

print("\ncar is the same as car2? I predict False")
print(car == car2)

car3 = "BMW"
print("\nIs car3 is in cars? I predict True")
print(car3.casefold() in cars)

print("\nIs car3 is in cars? I predict True")
print(car3.lower() in cars)

age_1 = 25
age_2 = 12
print("\nIs at least one older than 21? I predict True")
print(age_1 >= 25 or age_2 >= 25)

age_1 = 18
print("\nIs at least one older than 21? I predict False")
print(age_1 >= 25 or age_2 >= 25)

print("\nAre both 'audi' and 'suburu' in cars? I predict True")
print('audi' in cars and 'suburu' in cars)
