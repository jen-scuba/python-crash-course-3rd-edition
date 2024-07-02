from pathlib import Path
import json

path = Path('fav_number.txt')
contents = path.read_text()
number = json.loads(contents)
print(f"I know your favorite number! It's {number}.")