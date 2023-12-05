from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self.connection = connection
        
    def all(self):
        rows = self.connection.execute('SELECT * FROM artists')
        return [
            Artist (row['id'], row['name_artist'], row['genre'])
            for row in rows
        ]
        
    def create(self, artist):
        self.connection.execute(
            'INSERT INTO artists (name_artist, genre)VALUES (%s, %s)',
            [artist.name_artist, artist.genre]
            )
        return None