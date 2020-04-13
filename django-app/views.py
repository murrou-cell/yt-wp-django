from django.shortcuts import redirect
from pytube import YouTube
def out(request,videoID):
	yt = YouTube('https://www.youtube.com/watch?v=' + videoID)
	url=yt.streams.filter(only_audio=True)[0].url
	response = redirect(url)
	return response
