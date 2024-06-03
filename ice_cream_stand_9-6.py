from classes_91 import Restaurant


class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand with restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initalize attribute of the parent class.
        Then initialize attribute specifc to an Ice Cream Stand.
        """

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "swirl"]

    def show_flavors(self):
        """Show list of ice cream flavors vailable."""
        print(self.flavors)


my_stand = IceCreamStand("Dairy Delights", "ice cream")
my_stand.show_flavors()