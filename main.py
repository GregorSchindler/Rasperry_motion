#import numpy
import random as rn

# import RPi.GPIO as GPIO
import youtube_dl
import pafy
import vlc
import numpy

while 1:
    test = rn.randint(0,1)
    if test == 1:
        #mixer.init()
        #mixer.music.load('boom.wav')
        #mixer.music.play()
        url = "https://www.youtube.com/watch?v=WddpRmmAYkg&t=1519s"
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url

        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()


