import random as rn
import numpy as np
# import RPi.GPIO as GPIO
import youtube_dl
import pafy
import vlc
import time
import numpy


#while 1:
test = rn.randint(0,1)


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
time.sleep(15000)




