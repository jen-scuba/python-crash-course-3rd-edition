# verify the user before printing welcome back message....for 10-13 User dictionary
from pathlib import Path
import json


def get_stored_userdata(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        userdata = json.loads(contents)
        return userdata
    else:
        return None


def get_new_userdata(path):
    """Prompt for a new userdata."""
    username = input("What's your username? ")
    f_name = input("What's your first name? ")
    l_name = input("What's your last name? ")

    userdata = {'username': username,
                'firstname': f_name, 
                'lastname': l_name,
                }

    contents = json.dumps(userdata)
    path.write_text(contents)
    return userdata


def greet_user():
    """Greet the user by name."""
    path = Path('UserDictionary-ch10-13.txt')
    userdata = get_stored_userdata(path)
    if userdata:
        username = userdata.get('username')
        verify_username = input("Please type your username for verfication: ")
        if username != verify_username:
            userdata = get_new_userdata(path)
            name = userdata.get('firstname')
            print(f"We'll remember you when you come back, {name}!")
        else:
            name = userdata.get('firstname')
            print(f"Welcome back, {name}.")
            print(userdata)
    else:
        userdata = get_new_userdata(path)
        name = userdata.get('firstname')
        print(f"We'll remember you when you come back, {name}!")


greet_user()