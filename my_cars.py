"""Chapter 9 importing classes (module)"""

# from car_module import Car, ElectricCar

# my_leaf = ElectricCar("nissan", "leaf", 2024)
# print(my_leaf.get_descriptive_name())

# my_mustang = Car("ford", "mustang", 2024)
# print(my_mustang.get_descriptive_name())

import car_module

my_leaf = car_module.ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

my_mustang = car_module.Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())
