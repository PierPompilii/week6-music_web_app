from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_all(db_connection):
    db_connection.seed('seeds/record_store.sql')
    repository = ArtistRepository (db_connection)
    assert repository.all() == [
        Artist(1, 'Tool', 'Rock'),
        Artist(2, 'Mastodon', 'Rock')
    ]
    
def test_create (db_connection):
    db_connection.seed('seeds/record_store.sql')
    repository = ArtistRepository (db_connection)
    artist = Artist(None, 'name_artist', 'genre')
    repository.create(artist)
    assert  repository.all() == [
        Artist(1, 'Tool', 'Rock'),
        Artist(2, 'Mastodon', 'Rock'),
        Artist(3, 'name_artist', 'genre')
        ]