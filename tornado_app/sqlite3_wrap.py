import sqlite3 as sql

class Sqlwrapper():
	def __init__(self):
		self.db = sql.connect('music.db', check_same_thread=False)
		self.db2 = sql.connect('playlist.db', check_same_thread=False)

	'''Creates a new database to hold users media directory
		table should exist when app is started but should not hold any data'''
	def createMusicTable(self):
		self.db.execute("DROP TABLE Music")
		self.db.execute('''CREATE TABLE Music(
		   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
		   ARTIST           TEXT,
		   ALBUM            TEXT,       
		   GENRE			TEXT,
		   TRACKNUM			TEXT,
		   FILEPATH			TEXT,
		   FILENAME			TEXT
		)''')

	def addSong(self, artist, album,  genre, tracknum, filepath, filename):
		query = "INSERT INTO Music VALUES(null,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')"%(artist, album, genre, tracknum, filepath, filename)
		self.db.execute(query)

	def getByID(self, id):
		query = "SELECT * FROM Music where ID=%d"%(id)
		return self.db.execute(query)

	def getByArtist(self, artist):
		query = "SELECT * FROM Music where ARTIST=\'%s\'"%(artist)
		return self.db.execute(query)

	def getByAlbum(self, album):
		query = "SELECT * FROM Music where ALBUM=\'%s\'"%(album)
		return self.db.execute(query)

	def getByGenre(self, genre):
		query = "SELECT * FROM Music where GENRE=\'%s\'"%(genre)
		return self.db.execute(query)

	def getByFilePath(self, filepath):
		query = "SELECT * FROM Music where FILEPATH=\'%s\'"%(filepath)
		return self.db.execute(query)

	def getByFileName(self, filename):
		query = "SELECT * FROM Music where FILENAME=\'%s\'"%(filename)
		return self.db.execute(query)

	def getAllSongs(self):
		query = "SELECT * FROM Music"
		return self.db.execute(query)
	def search():
		pass
		

	'''Database holds users playlists etc... Database '''
	def createPlayLTable(self):
		self.db.execute('''CREATE TABLE IF NOT EXISTS Music(
		   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
		   NAME 			TEXT,
		   FILEPATH         TEXT
		)''')

	def addToPlayList():
		pass

	def getAPlayList():
		pass

	def getPlayLists():
		pass



