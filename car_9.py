class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # 3 ways to modify attribute value
    # 2 - directly through a method
    def update_odometer(self, mileage):
        """Set the odometer reading to a given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # 3 - increment through a method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


# my_new_car = Car("audi", "a4", 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# # 3 ways to modify attribute value
# # 1 - directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# # 2 - directly through a method
# my_new_car.update_odometer(24)
# my_new_car.read_odometer()

# # 3 - incrementing value through a method
# my_used_car = Car("subaru", "outback", 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(-1)
# my_used_car.read_odometer()