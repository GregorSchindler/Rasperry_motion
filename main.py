#import numpy
import time
import os
import random as rn
#import RPi.GPIO as GPIO
from pygame import mixer
import playsound


while 1:
    test = rn.randint(0,1)
    if test == 1:
        mixer.init()
        mixer.music.load('boom.wav')
        mixer.music.play()


