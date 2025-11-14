def make_album(artist_name, album_title, number_of_songs=None):
    """ Build a dictionart describing a music album. """
    album = {
        'artist': artist_name,
        'title': album_title
        }
    
    if number_of_songs:
        album['songs'] = number_of_songs
        
    return album

# Make three dictionaries representing different albums
album1 = make_album('The beatles', 'Abbey Road')
album2 = make_album('Pink Floyd', 'The Dark Side of the Moon')
album3 = make_album('Queen', 'A night at the Opera')

print(album1)
print(album2)
print(album3)

# Make a function call that includes the number of songs
album4 = make_album('Michael Jackson', 'Thriller', 9)
print(album4)