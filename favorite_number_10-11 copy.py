from pathlib import Path
import json

number = input("What's your favorite number? ")
path = Path('fav_number.txt')
contents = json.dumps(number)
path.write_text(contents)