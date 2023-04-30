#!/Users/rebontadeb/opt/anaconda3/bin/python3

import sys,os
from pytube import YouTube,Playlist
SAVE_PATH='/yt-download/downloads'
arg = sys.argv[1]
playlist = Playlist(arg)


print('Number of videos in playlist: %s' % len(playlist.video_urls))
count = 0

for video in playlist.video_urls:
  video_dl = YouTube(video,use_oauth=True, allow_oauth_cache=True)
  stream = video_dl.streams.get_highest_resolution()
  stream.download(SAVE_PATH)
  count=count+1
  print (count," video downloaded : ",video_dl.title)
