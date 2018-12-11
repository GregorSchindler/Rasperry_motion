import random as rn

# import gdata

# import RPi.GPIO as GPIO
import youtube_dl
import pafy
import vlc
import time as timer
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

from datetime import datetime, date, time
import requests
import json


def main():
    actual_time = datetime.now().time()
    vidID = ''
    # Check time
    if time(9) > actual_time:
        # find song for morning
        print('morning')
        vidID = find_song('morning')
    elif time(16) > actual_time:
        # find song for during day
        print('day')
        vidID = find_song('happy')
    elif time(22) > actual_time:
        print('evening')
        vidID = find_song('party')
    else:
        # song for night
        print('night')
        vidID = find_song('musik party')

    url = vidID
    video = pafy.new(url)
    best = video.getbestaudio()
    playurl = best.url

    instance = vlc.Instance("--no-xlib")
    player = instance.media_player_new()
    media = instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)
    player.play()
    timer.sleep(10)
    player.stop()


def find_song(keyword):
    argparser.add_argument("--q", help=keyword)
    argparser.add_argument("--max-results", help="Max results", default=25)
    args = argparser.parse_args()


    try:
        vidID = youtube_search(args)
    except:
        print("An HTTP error %d occurred:\n%s")
    return vidID

def youtube_search(options):
    DEVELOPER_KEY = ""
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))
            vidID = search_result["id"]["videoId"]
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                         search_result["id"]["channelId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                          search_result["id"]["playlistId"]))

    print("Videos:\n", "\n".join(videos), "\n")
    #print("Channels:\n", "\n".join(channels), "\n")
    #print("Playlists:\n", "\n".join(playlists), "\n")
    print(vidID)
    return vidID

main()
