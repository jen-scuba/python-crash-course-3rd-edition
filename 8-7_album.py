def make_album(name, title, num_songs=None):
    if num_songs:
        album = {'artist': name , 'title': title, 'number_songs': num_songs }
    else:
        album = {'artist': name , 'title': title}
    return album

album = make_album('carpenters','rainy days and mondays',12)
print(album)
album = make_album('beatles','white album')
print(album)
album = make_album('prince and the revolution','purple rain')
print(album)