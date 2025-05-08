import urllib
import urllib2
import json

API_KEY = 'AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg'

searchTerm = raw_input('Search for a term: ')

searchTerm = urllib.quote_plus(searchTerm) #turns non word characters into url-safe characters

url = 'https://www.googleapis.com/customsearch/v1?q='+searchTerm+'&key='+API_KEY

response = urllib2.urlopen(url) #makes the call to YouTube

videos = json.load(response) #decodes the response so we can work with it

print videos
# videoMetadata = [] #declaring our list

# for video in videos['items']:
#     if video['id']['kind'] == 'youtube#video':
#         videoMetadata.append(video['snippet']['title']+
#         "\nDescription:"+video['snippet']['description']+
#         "\nPublished date:"+video['snippet']['publishedAt']+
#         "\nhttp://youtube.com/watch?v="+video['id']['videoId'])
        

# videoMetadata.sort();

# print "\nSearch Results:\n"

# for metadata in videoMetadata:
#     print metadata+"\n"

# raw_input('Press Enter to Exit')