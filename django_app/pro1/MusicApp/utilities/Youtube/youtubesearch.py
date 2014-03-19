import yss

from MusicApp.LocalAudio.audio import Uaudio
from django import template
from searchops import Option

class Youtube:
	
	def getSearchIDS(self, searchTerms):
		ops = Option()
		ops.q = searchTerms
		ops.max_results = 9
		jsonRe = yss.youtube_search(ops)
		searchIDS = []
		for i in range(ops.max_results):
			if jsonRe['items'][i]['id'].has_key('videoId'):
				path = jsonRe['items'][i]['id']['videoId']
				title = jsonRe['items'][i]['snippet']['title']
								
				youAudio = Uaudio(title, path)
				searchIDS.append(youAudio)
			
		
		return searchIDS
