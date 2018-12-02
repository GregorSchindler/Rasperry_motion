import random as rn
import numpy as np
# import RPi.GPIO as GPIO
import youtube_dl
import pafy
import vlc
import time as timer
import numpy
from datetime import datetime, date, time
import requests
import json



def main():
    actual_time = datetime.now().time()
    print(actual_time)

    # Check time
    if time(9) > actual_time:
        # find song for morning
        print('morning')
    elif time(16) > actual_time:
        # find song for during day
        print('day')
        find_song()
    elif time(22) > actual_time:
        print('evening')
        find_song()
    else:
        # song for night
        print('night')




    url = "https://www.youtube.com/watch?v=WddpRmmAYkg&t=1519s"
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    instance = vlc.Instance("--no-xlib")
    player = instance.media_player_new()
    media = instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)
    player.play()
    timer.sleep(10)
    player.stop()



def find_song():
    r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
    r.text
    print(r.text)
    # Convert it to a Python dictionary
    data = json.loads(r.text)

    # Loop through the result.
    for item in data['data']['items']:
        print("Video Title: %s" % (item['title']))

        print("Video Category: %s" % (item['category']))

        print("Video ID: %s" % (item['id']))

        print("Video Rating: %f" % (item['rating']))

        print("Embed URL: %s" % (item['player']['default']))

#while 1:
main()

