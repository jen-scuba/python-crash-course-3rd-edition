class Restaurant:
    """A simple Restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        "Provide a basic description of the restaurant"
        print(f"The {self.restaurant_name} servers {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


# my_restaurant = Restaurant("Outback Steak House", "American")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()


class User:
    """A simple user model"""

    def __init__(self, first_name, last_name, job, state):
        """Initialize basic attributes of a User."""
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.state = state

    def describe_user(self):
        """Provide a basic description of the user"""
        print(
            f"User: {self.first_name.title()} {self.last_name.title()} \n"
            f"Job: {self.job.title()} \n"
            f"State: {self.state.title()}"
        )

    def greet_user(self):
        """Provide a personal greeting for the user"""
        print(
            f"Welcome to the site {self.first_name.title()} {self.last_name.title()} "
            f"from {self.state.title()}!"
        )