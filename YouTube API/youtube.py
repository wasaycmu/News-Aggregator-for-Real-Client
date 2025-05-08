import os
import sys
import urllib
import urllib2
import json
import datetime
import time

def dateConverter(date):
    result=date[0:4]+date[5:7]+date[8:10]+date[11:13]+date[14:16]+date[17:19]
    return result

def youtube_get_urls(start_date, end_date):

    API_KEY = 'AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg'
    videoMetadata = []
    listOfSearchTerms = ["Qur'anic botanic garden", "Quranic botanic garden",
                         "quranic_botanic_garden", "QBG Qatar Foundation",
                         "quranic garden Qatar foundation", "Quranic botanic garden Qatar"]

    for searchTerm in listOfSearchTerms:
        searchTerm = urllib.quote_plus(searchTerm)
        url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&publishedAfter='+start_date+'&q='+searchTerm+'&key='+API_KEY
        response = urllib2.urlopen(url)
        videos = json.load(response)

        for video in videos['items']:
            
            if video['id']['kind'] == 'youtube#video':

                duplicate = False
                newVideoURL = "http://youtube.com/watch?v="+video['id']['videoId']
                
                for savedVideo in videoMetadata:
                    savedVideoURL = savedVideo[2]
                    if newVideoURL == savedVideoURL:
                        duplicate = True
                   
                if duplicate == False:
                    videoMetadata.append(
                        [
                            #dummy id 
                            0,
                            #url
                            ("http://youtube.com/watch?v="+video['id']['videoId']),
                            #retrieval date
                            str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
                            #description
                            video['snippet']['description'],
                            #data_file
                            video['snippet']['thumbnails']['default']['url'],
                            #publish date
                            dateConverter(video['snippet']['publishedAt']),
                            #title
                            video['snippet']['title'],
                            #source_id
                            3
                        ]

                        
                                         )
    #for metadata in videoMetadata:
        #print metadata[2]
    return videoMetadata





total_records = youtube_get_urls("2005-11-26T22:54:32.000Z","2017-11-26T22:54:32.000Z")
print total_records
print len(total_records)







