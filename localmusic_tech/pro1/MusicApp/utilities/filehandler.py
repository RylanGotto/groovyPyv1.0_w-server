import os

def readFile():
	f = open(os.getcwd() + '/MusicApp/settings.txt', 'r')
	path = f.read()
	path = path.rstrip('\n')
	return path	

def writeFile(path):
	f = open(os.getcwd() + '/MusicApp/settings.txt', 'w')
	f.write(path)
	
	
