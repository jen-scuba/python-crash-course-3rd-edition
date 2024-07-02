from pathlib import Path

def count_words(filename, search_word):
    # Display the number of times the user provided word appears in the 
    # user provided filename

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(search_word)
        print(f"The word {search_word} appears {word_count} times in {filename}.")

count_words('shakespeare.txt', 'art')
count_words('shakespeare.txt', ' art ')
count_words('huckleberryfinn.txt', 'river')
count_words('shakespeare.txt', 'the')
count_words('huckleberryfinn.txt', 'the')
count_words('shakespeare.txt', 'the ')
count_words('huckleberryfinn.txt', 'the ')


# filenames = ['shakespeare.txt', 'huckleberryfinn.txt']

# for f_name in filenames:
#     path = Path(f_name)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         pass
#     else:
#         word_count = contents.lower().count('the')
#         print(f"The word 'the' appears {word_count} times in {f_name}.")