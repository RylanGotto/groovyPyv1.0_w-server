import pymedia
import time


class PMwrapper(object):
	def __init__(self):
			self.player = pymedia.Player()

	def start_playloop(self):
			self.player.start()

	def stop(self):
			self.player.stopPlayback()

	def pause(self):
			self.player.pausePlayback()

	def unpause(self):
			self.player.unpausePlayback()

	def isPlaying(self):
			return self.player.isPlaying() 
	def isPaused(self):
			return self.player.isPaused()

	def play(self, path):
			self.player.startPlayback(path)


	
