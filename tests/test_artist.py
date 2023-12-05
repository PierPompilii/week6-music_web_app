from lib.artist import Artist

def test_artist_construct():
    artist = Artist (1, 'name_artist', 'genre')
    assert artist.id == 1
    assert artist.name_artist == 'name_artist'
    assert artist.genre == 'genre'
    
def test_equal_artist():
    artist_1 = Artist (1,'name_artist', 'genre')
    artist_2 = Artist (1,'name_artist', 'genre')
    assert artist_1 == artist_2
    
def test_string_for_artist():
    artist = Artist (1, 'name_artist', 'genre')
    assert str(artist) == "Artist(1, name_artist, genre)"