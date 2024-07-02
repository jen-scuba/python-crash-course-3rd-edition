from pathlib import Path

# original code
# path = Path('programming.txt')
# path.write_text("I love programming.")

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

# creates or overwrites the file if it exists
path = Path('programming.txt')
path.write_text(contents)