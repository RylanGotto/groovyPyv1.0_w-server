from audio import Audio
import songdetails
def buildAudioObj(path):
	af = songdetails.scan(path)
	mp3 = Audio(af.artist, af.album, af.genre, af.track, path)
	return mp3

