#!/Users/rebontadeb/opt/anaconda3/bin/python3


import sys, os
from pytube import YouTube, Playlist

SAVE_PATH = "/Users/rebontadeb/Documents/My_Docs.nosync/youtube_video/trial-mp3"
arg = sys.argv[1]
playlist = Playlist(arg)
os.makedirs(SAVE_PATH, exist_ok=True)


print("Number of videos in playlist: %s" % len(playlist.video_urls))
count = 0

choice = input("Choose type of Download A=Audio|V=Video : ").lower()

if choice == "a":
    for video in playlist.video_urls:
        video_dl = YouTube(video, use_oauth=True, allow_oauth_cache=True)
        stream = video_dl.streams.filter(only_audio=True).first()
        out_file = stream.download(SAVE_PATH)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        count = count + 1
        print(count, " Audio downloaded : ", new_file)
elif choice == "v":
    for video in playlist.video_urls:
        video_dl = YouTube(video, use_oauth=True, allow_oauth_cache=True)
        stream = video_dl.streams.get_highest_resolution()
        stream.download(SAVE_PATH)
        count = count + 1
        print(count, " video downloaded : ", video_dl.title)
else:
    print("Wrong Choice")
