from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

# lines = contents.splitlines()
pi_string = ''
# for line in lines:
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("your birthday appears in the first milion digits of pi!")
else:
    print("your birthday does not appear in the first milion digits of pi.")
