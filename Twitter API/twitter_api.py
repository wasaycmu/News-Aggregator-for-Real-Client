#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import the necessary package to process data in JSON format
import json
import urllib2

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


def youtube_get_urls(listOfSearchTerms):
    # Variables that contains the user credentials to access Twitter API 
    ACCESS_TOKEN = '866202573900058624-0IoFWFQLtMIAuYOiFyHyoob7NKJsQ9z'
    ACCESS_SECRET = 'NnHTbOlva1m5whiDd3Fdm36MY9heOyyBM9jjQrf6WvUwK'
    CONSUMER_KEY = '4N7JQbtm6T8Lh216TfFFE1diK'
    CONSUMER_SECRET = 'DHPrpv7qAZqWBW5uKDdlXQFAT2WYllUA5NkG1Ow7OvraUcEBGf'

    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    listOfSearchTerms.append('QuranicGarden')
    listOfSearchTerms.append('@QuranicGarden')

    # Initiate the connection to Twitter Streaming API
    twitter = Twitter(auth=oauth)

    data = []
    #print twitter
    # Quranic tweets

    for searchTerm in listOfSearchTerms:

        tweets_col = twitter.search.tweets(q=searchTerm, count=100, result_type='recent')

        #print len(tweets_col['statuses'])

        for i in range(0, len(tweets_col['statuses'])):
            data.append( 

                #title
                tweets_col['statuses'][i]['text'],
                #url

                #archive url

                #retrieval date

                #description

                #file_path

                #publish date

                #source_id

                #tag

                #event
                )

    return data

print "the length" + str(len(youtube_get_urls([]))) + '\n'
print youtube_get_urls([])





 