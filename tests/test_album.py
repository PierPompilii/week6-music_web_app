from lib.album import Album

def test_album_construct():
    album = Album (1, 'title', 2000, 1)
    assert album.id == 1
    assert album.title == 'title'
    assert album.release_year == 2000
    assert album.artist_id == 1
    
    
def test_equal():
    album_1 = Album (1,'title', 2000, 1)
    album_2 = Album (1,'title', 2000, 1)
    assert album_1 == album_2
    
def test_string():
    album = Album(1, "title", 2000, 1)
    assert str(album) == "Album(1, title, 2000, 1)"