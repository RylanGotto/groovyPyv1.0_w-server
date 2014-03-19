
import ntpath
class Audio:
    def __init__(self, artist, album, genre, trackNum, path):
		self.artist = artist
		self.album = album 
		self.genre = genre
		self.tracknum = trackNum
		self.filepath = path
		self.filename = ntpath.basename(path)