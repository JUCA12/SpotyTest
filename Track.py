
class Track:

    def __init__(self,id, name, artist, album, duration):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        if self.id != None:
            return str(f"El track es: {self.name}" +
                      f" de {self.artist}"+
                       f" del album {self.album}")
