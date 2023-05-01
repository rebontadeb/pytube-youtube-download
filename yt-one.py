#!/Users/rebontadeb/opt/anaconda3/bin/python3

from pytube import YouTube

SAVE_PATH = "/Users/rebontadeb/Documents/My_Docs.nosync/youtube_video/"
inp = input("Prompt:")
link = []
# link=["https://www.youtube.com/watch?v=T4Df5_cojAs&ab_channel=kubucation"]
link.append(inp.strip())

for i in link:
    video_obj = YouTube(i, use_oauth=True, allow_oauth_cache=True)
    stream = video_obj.streams.get_highest_resolution()
    # stream = video_obj.streams.filter(only_audio=True).first()
    try:
        stream.download(SAVE_PATH)
        print("Task Completed")
    except:
        print("Some Error!")
