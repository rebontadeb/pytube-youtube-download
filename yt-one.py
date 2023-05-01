#!/Users/rebontadeb/opt/anaconda3/bin/python3
import os
from pytube import YouTube

SAVE_PATH = "/Users/rebontadeb/Documents/My_Docs.nosync/youtube_video/"
inp = input("Video Link :")
link = []
link.append(inp.strip())


choice = input("Choose type of Download A=Audio|V=Video : ").lower()

if choice == "a":
    for i in link:
        video_obj = YouTube(i, use_oauth=True, allow_oauth_cache=True)
        # stream = video_obj.streams.get_highest_resolution()
        stream = video_obj.streams.filter(only_audio=True).first()
        try:
            out_file = stream.download(SAVE_PATH)
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
            print("Task Completed")
        except:
            print("Some Error!")
elif choice == "v":
    for i in link:
        video_obj = YouTube(i, use_oauth=True, allow_oauth_cache=True)
        stream = video_obj.streams.get_highest_resolution()
        try:
            stream.download(SAVE_PATH)
            print("Task Completed")
        except:
            print("Some Error!")
else:
    print("Wrong Choice")
