places = ['heidlberg','florence','new zealand','komodo','yellowstone']
print(places)

print("\nHere is the places list temporarily sorted")
print(sorted(places))

print("\nHere is the original list again")
print(places)

print("\nHere is the places list temporarily corted in reverse")
print(sorted(places,reverse=True))

print("\nHere is the original list again")
print(places)

print("\nHere is the list in permanent reverse order")
places.reverse()
print(places)

print("\nHere is the list permanently reversed back in original order")
places.reverse()
print(places)

print("\nHere is the list permanently sorted alhabetically")
places.sort()
print(places)

print("\nHere is the list permanently sorted in reverse alhabetically")
places.sort(reverse=True)
print(places)

