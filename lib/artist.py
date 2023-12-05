class Artist():
    def __init__(self, id, name_artist, genre):
        self.id = id
        self.name_artist = name_artist
        self.genre = genre
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Artist({self.id}, {self.name_artist}, {self.genre})'
        