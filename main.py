import random as rn
import numpy as np
# import RPi.GPIO as GPIO
import youtube_dl
import pafy
import vlc
import time as timer
import numpy
from datetime import datetime, date, time


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
    elif time(22) > actual_time:
        print('evening')
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


#while 1:
main()

