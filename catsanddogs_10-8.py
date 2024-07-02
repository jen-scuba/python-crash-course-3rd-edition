from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for f_name in filenames:
    """ Print the conents fo each file. """
    path = Path(f_name)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        # if we want to tell the user a file is missing...
        # print(f"The file {path} was not found.")
        # if we don't - file silently and move on
        pass
    else:
        for line in contents.splitlines():
            print(line)