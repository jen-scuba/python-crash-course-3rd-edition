alien_0 = {'color': 'green', 'speed': 'slow'}

print(alien_0)
            
''' until chapter 10 (try/catch/except...) 
    use default value on get() for non-existent keys instead of 
    square bracket notation.
'''

point_value = alien_0.get('points', 'no point value assigned.')
print(point_value)

point_value_2 = alien_0.get('points')
print(point_value_2)
