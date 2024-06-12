"""Chapter 9 9-12"""

"""admin_module imports User from classes_91 module"""
from admin_module import Admin


admin_1 = Admin("Jane", "Doe", "Site Admininstrator", "Maryland")
admin_1.privileges.show_privileges()
admin_1.describe_user()
