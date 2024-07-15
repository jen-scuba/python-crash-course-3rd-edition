import pytest
from employee_ch11 import Employee


@pytest.fixture
def employee():
    employee = Employee('Jane', 'Doe', 20000)
    return employee


def test_give_default_raise(employee):
    """Test that a raise of the default amount updates salary properly"""
    employee = Employee('Jane', 'Doe', 20000)
    employee.give_raise()
    assert employee.annual_salary == 25000 


def test_give_custom_raise(employee):
    """Test that a raise of a give amount updates salary properly"""
    employee = Employee('Jane', 'Doe', 20000)
    employee.give_raise(7500)
    assert employee.annual_salary == 27500
