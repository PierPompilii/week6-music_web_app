
from lib.album_repository import AlbumRepository
from lib.album import Album


def test_all(db_connection):
    db_connection.seed('seeds/record_store.sql')
    repository = AlbumRepository (db_connection)
    assert repository.all() == [
        Album (1, 'Lateralus', 2001, 1)
    ]
    
def test_create (db_connection):
    db_connection.seed('seeds/record_store.sql')
    repository = AlbumRepository (db_connection)
    album = Album(None, 'title', 2000, 2)
    repository.create(album)
    assert  repository.all() == [
        Album(1, 'Lateralus', 2001, 1),
        Album (2, 'title', 2000, 2)
    ]