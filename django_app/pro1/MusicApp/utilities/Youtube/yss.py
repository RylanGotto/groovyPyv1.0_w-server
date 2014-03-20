#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBXbs5mgupCQvA7CJkyu08hCoFF3P4_ock"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
vids = {}
for search_result in search_response.get("items", []):
	if search_result["id"]["kind"] == "youtube#video":
		videos.append("%s %s %s" % (search_result["snippet"]["title"],
                             search_result["id"]["videoId"],
                             search_result["snippet"]["thumbnails"]['medium']['url']))
   
      


  return search_response






def getz(search_response):
	videos = []
		for search_result in search_response.get("items", []):
			if search_result["id"]["kind"] == "youtube#video":
				videos.append("%s %s %s" % (search_result["snippet"]["title"],
		                             search_result["id"]["videoId"],
		                             search_result["snippet"]["thumbnails"]['medium']['url']))
	return videos



search_result["id"]["videoId"]
search_result["snippet"]["title"]
search_result["snippet"]["thumbnails"]['medium']['url'] 