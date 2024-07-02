from pathlib import Path

name = input("Please type your first name. ")

path = Path('guest.txt')
path.write_text(name)