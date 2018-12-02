import random as rn

#import gdata

# import RPi.GPIO as GPIO
import youtube_dl
import pafy
import vlc
import time as timer

from datetime import datetime, date, time
import requests
import json


def main():
    actual_time = datetime.now().time()

    # Check time
    if time(9) > actual_time:
        # find song for morning
        print('morning')
        find_song('morning')
    elif time(16) > actual_time:
        # find song for during day
        print('day')
        find_song('happy')
    elif time(22) > actual_time:
        print('evening')
        #find_song('party')
    else:
        # song for night
        print('night')
        find_song('party')

    url = "https://www.youtube.com/watch?v=WddpRmmAYkg&t=1519s"
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


def find_song(list_of_search_terms):
    user_agent = {'User-Agent': 'Firefox/60.0'}
    r = requests.get('http://music.youtube.com/search?q=' + list_of_search_terms, headers=user_agent)
    texts = r.text
    print(r.text)
    print(r.status_code)
    url = ''
    return url


    #
    # yt_service = gdata.youtube.service.YouTubeService()
    # query = gdata.youtube.service.YouTubeVideoQuery()
    # query.orderby = 'viewCount'
    # query.racy = 'include'
    # for search_term in list_of_search_terms:
    #     new_term = search_term.lower()
    #     query.categories.append('/%s' % new_term)
    # feed = yt_service.YouTubeQuery(query)
    # printVideoFeed(feed)


def printVideoFeed(feed):
    for entry in feed.entry:
        printEntryDetails(entry)


def printEntryDetails(entry):
    print('Video title: %s' % entry.media.title.text)
    print('Video published on: %s ' % entry.published.text)
    print('Video description: %s' % entry.media.description.text)
    print('Video category: %s' % entry.media.category[[0]].text)
    print('Video tags: %s' % entry.media.keywords.text)
    print('Video watch page: %s' % entry.media.player.url)
    print('Video flash player URL: %s' % entry.GetSwfUrl())
    print('Video duration: %s' % entry.media.duration.seconds)

    # non entry.media attributes
    print('Video geo location: %s' % entry.geo.location())
    print('Video view count: %s' % entry.statistics.view_count)
    print('Video rating: %s' % entry.rating.average)

    # show alternate formats
    for alternate_format in entry.media.content:
        if 'isDefault' not in alternate_format.extension_attributes:
            print('Alternate format: %s | url: %s ' % (alternate_format.type,
                                                       alternate_format.url))

    # show thumbnails
    for thumbnail in entry.media.thumbnail:
        print('Thumbnail url: %s' % thumbnail.url)


# while 1:
main()
