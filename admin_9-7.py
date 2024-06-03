from classes_91 import User


class Privileges:
    """A simple attempt to model a privileges."""

    def __init__(
        self, privileges_list=["can add post", "can delete post", "can ban user"]
    ):
        """Initialize the attributes of privileges."""
        self.privileges_list = privileges_list

    def show_privileges(self):
        """Print the list of privilges assigned to the Admin."""
        print(self.privileges_list)


class Admin(User):
    """Represent aspects of an Admin user."""

    def __init__(self, first_name, last_name, job, state):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an Admin.
        _summary_

        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            job (_type_): _description_
            state (_type_): _description_
        """
        super().__init__(first_name, last_name, job, state)
        self.privileges = Privileges()


admin_1 = Admin("Jane", "Doe", "Site Admininstrator", "Maryland")
# admin_1.show_privileges()
admin_1.describe_user()
admin_1.privileges.show_privileges()
