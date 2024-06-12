"""A set of classes from chapter 9 that represent Restaurant."""


class Restaurant:
    """A simple Restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        "Provide a basic description of the restaurant"
        print(f"The {self.restaurant_name} servers {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def read_number_served(self):
        """Print a statement showing the car's mileage."""
        print(f"The number of patrons served is {self.number_served}.")

    def set_number_served(self, just_served):
        "Set the number served to a given number." ""
        self.number_served = just_served

    def increment_number_served(self, additional_served):
        """Add given amount to the number served today."""
        if additional_served >= 0:
            self.number_served += additional_served
        else:
            print("You can't serve a negative number of additional customrs!")
