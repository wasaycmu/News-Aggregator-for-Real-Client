# Get the first 10 hits
from google import search
import datetime
import time
import requests
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import urllib2
import lxml.html


for url in search('quranic botanic garden', tld='com', stop=10):
	print url
	t = lxml.html.parse(url)
	print t.find(".//title").text

	# response = urllib2.urlopen(url)
	# #print "The Headers are: ", response.info()
	# html = response.read()
	# print "Get all data: ", html

	#print f.text


# import urllib
# import urllib2
# import json

# #test url
# #https://www.googleapis.com/customsearch/v1?key=AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg&cx=000449499422531286556:exjmwogp3qm&q=Quranic+Botanic+Garden
# API_KEY = 'AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg'
# cx = '000449499422531286556:exjmwogp3qm'
# searchText = "Qur'anic Botanic Garden"

# url = "https://www.googleapis.com/customsearch/v1?key="+API_KEY+"&cx="+cx+"&q="+searchText+"&alt=json"+"&start="+str(0)+"&num="+str(30)

# response = requests.get(url)

# print response
#videos = json.loads(response) #decodes the response so we can work with it

#print videos
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


# def google_get_urls(start_date, end_date):
# 	records_list = []


# 	ind_tuple = (0, "google", "sample_url", "sample_title", "sample_des", 
# 		'start_date', 'end_date', None)

# 	records_list.append(ind_tuple)

# 	print records_list



# 	print type(start)










#for url in search('quranic botanic garden', tld='com', stop=10):
#    print(url)

# import pdfkit
# pdfkit.from_url('http://google.com', 'out.pdf')


#Date time things
# datetime.datetime.now().strftime('%Y %m %d %H %M %S')
# print str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

# start_date = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
# start = datetime.datetime.strptime(start_date, '%Y%m%d%H%M%S')
# end = datetime.datetime.now()
# print type(start)

#print int(time.mktime(datetime.datetime.now().timetuple()))