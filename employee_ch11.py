class Employee():
    """A simple Employee respresentation"""

    def __init__(self,first, last, salary):
        self.firstname = first
        self.lastname = last
        self.annual_salary = salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount
