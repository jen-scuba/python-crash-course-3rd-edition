from pathlib import Path
import json

path = Path('fav_number.txt')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
else:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print(f"We'll remember it for you.")