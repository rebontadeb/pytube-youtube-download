FROM alpine:latest
RUN apk update
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN python -m pip install --upgrade pip 
RUN pip install pytube
RUN mkdir -p /yt-download/script
RUN mkdir -p /yt-download/downloads
COPY yt-play.py /yt-download/script/.
RUN chmod +x /yt-download/script/yt-play.py
ENTRYPOINT ["python","/yt-download/script/yt-play.py"]
