from pathlib import Path

path = Path('guest_book.txt')
guests = ''

while True:
    name = input("Welcome! Please type your name for the Guest Book.\n"
                 "If there are no more guests, please type 'None'. ")

    if name == "None":
        print("Thank you for entering your name in the Guest Book!")
        break
    else:
        guests += name + "\n"

path.write_text(guests)