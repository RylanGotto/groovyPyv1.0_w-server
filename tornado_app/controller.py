from sqlite3_wrap import Sqlwrapper
from pymedia_wrap import PMwrapper

import time


class Control(object):
	def __init__(self):
		self.db = Sqlwrapper()
		self.player = PMwrapper()

	def loadDB(self, path): # will take path provided by the user
		mp3s = []
		mp3paths = local_search.get_filepaths(path)
		for path in mp3paths:
			mp3s.append(audiobuilder.buildAudioObj(path))
		self.db.createMusicTable()
		for mp3 in mp3s:
			self.db.addSong(mp3.artist,mp3.album,mp3.genre,mp3.tracknum,mp3.filepath,mp3.filename)

	def getMusicList(self):
		mp3s = []
		for name in self.db.getAllSongs():
			mp3s.append(audiobuilder.buildAudioObj(name[5]))
			mp3s.sort()
		return mp3s

	def searchDB():
		pass

	def start(self): # starts player loop
		self.player.start_playloop()

	def playsong(self, path):
		self.player.stop()
		while not self.player.isPlaying():
			time.sleep(0.05) # allow half second for pymedia to release its head from its rectum
			self.player.play(path)
	def stop(self):
		self.player.stop()
	def pause(self):
		self.player.pause()
	def unpause(self):
		self.player.unpause()
	def isPaused(self):
		return self.player.isPaused()
	def isPlaying(self):
		return self.player.isPlaying()


