from pathlib import Path


def count_words(filename):
    try:
        contents = path.read_text(encoding='utf8')
    except FileNotFoundError:
        # if we want to print a message
        # print(f"Sorry, the file {path} does not exist.")
        # if we don't just pass
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 
             'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)
