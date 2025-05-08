#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import requests
import datetime
#test url
#url_org = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg&cx=000449499422531286556:exjmwogp3qm&q=Quranic+Botanic+Garden'



def facebook_data(listOfSearchTerms):




    API_KEY = 'AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg'
    cx = '000449499422531286556:pudnujlzv5s'
    searchText = "Quranic Botanic Garden site:facebook.com"

    searchTerm = urllib.quote_plus(searchText)

    #Starting result index
    page_index = 1
    url = "https://www.googleapis.com/customsearch/v1?key="+API_KEY+"&cx="+cx+"&q="+searchTerm+"&start="+str(page_index)
    #print url
    response = urllib2.urlopen(url)

    fb_urls = json.load(response) #decodes the response so we can work with it

    # soup = BeautifulSoup(html_string, 'lxml')
    # table = soup.find_all('table')[0]

    #print fb_urls

    facebook_data_list = [] 
    next_page = 10

    total_results = fb_urls['queries']['request'][0]['totalResults']
    print "Total results for this search:\n" + total_results

    if total_results > 100:
        total_results = 9
    else:
        total_results = total_results - 1

    print "loops\n" + str(total_results) 


    for listLength in range(0,10):
        while(int(fb_urls['queries']['request'][0]['totalResults']) > 0 and page_index < 90):
            page_index = page_index + 10
            #Loading the page number
            url = "https://www.googleapis.com/customsearch/v1?key="+API_KEY+"&cx="+cx+"&q="+searchTerm+"&start="+str(page_index)
            print url
            response = urllib2.urlopen(url)
            fb_urls = json.load(response)
            print "total for this page:" + fb_urls['queries']['request'][0]['totalResults']
            print "Records processed:"
            print page_index
            print "\n"

            if int(fb_urls['queries']['request'][0]['totalResults']) > 0:
                for index in range(0,int(fb_urls['queries']['request'][0]['count'])):

                                    facebook_data_list.append(
                                        (
                                            #title
                                            fb_urls['items'][index]['title'],

                                            #url
                                            fb_urls['items'][index]['link'],

                                            #archive_url
                                            'https://web.archive.org/web/*/'+str(fb_urls['items'][index]['link']),

                                            #retrieval date
                                            str(datetime.date.today()),

                                            #description
                                            fb_urls['items'][index]['snippet'],

                                            #file_path
                                            None,

                                            #published_date
                                            None,
                                            #source_id
                                            1,
                                            #tag id,
                                            1,
                                            #event
                                            1
                                        )
                                                         )
        #Iterating through search terms
        #searchTerm = urllib.quote_plus(listOfSearchTerms[listLength])
    
    return facebook_data_list

# f = facebook_data([])
# print f
# print len(f)


