def make_album(name, title):
    album = {'artist': name , 'title': title}
    return album


while True:
    print("\nPlease tell me your favorite music artist name: ")
    print("(enter 'q' at any time to quit)")
    
    a_name = input("artist: " )
    if a_name == 'q':
        break
    
    print(f"\nWhat's the title of your favorite album by {a_name.title()}: ")
    print("(enter 'q' at any time to quit)")
    
    a_title = input("artist: " )
    if a_name == 'q':
        break
    
    favorite_album = make_album(a_name, a_title)
    print(favorite_album)
    