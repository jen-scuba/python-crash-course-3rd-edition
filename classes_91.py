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
        self.login_attempts = 0

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

    def read_login_attempts(self):
        """Print the number of login attempts."""
        print(f"Number of logins attempted: {self.login_attempts}.")

    def increment_login_attempts(self):
        """increment login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0
