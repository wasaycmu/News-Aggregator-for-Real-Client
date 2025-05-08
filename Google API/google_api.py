import urllib
import urllib2
import json
import requests
import datetime
#test url
#url_org = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg&cx=000449499422531286556:exjmwogp3qm&q=Quranic+Botanic+Garden'



def google_data(startDate):

    API_KEY = 'AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg'
    cx = '000449499422531286556:exjmwogp3qm'
    searchText = "qur'anic botanic garden"

    searchTerm = urllib.quote_plus(searchText)

    #Starting result index
    page_index = 1
    url = "https://www.googleapis.com/customsearch/v1?key="+API_KEY+"&cx="+cx+"&q="+searchTerm+"&start="+str(page_index)
    print url
    response = urllib2.urlopen(url)

    google_urls = json.load(response) #decodes the response so we can work with it

    # soup = BeautifulSoup(html_string, 'lxml')
    # table = soup.find_all('table')[0]

    #print google_urls

    google_data_list = [] 

    total_results = google_urls['queries']['request'][0]['totalResults']
    print total_results



    for total in range(0, 1):#int(total_results)/10):
        
        page_index = page_index + 10
        #Loading the page number
        url = "https://www.googleapis.com/customsearch/v1?key="+API_KEY+"&cx="+cx+"&q="+searchTerm+"&start="+str(page_index)
        print url
        response = urllib2.urlopen(url)
        google_urls = json.load(response)

        print "Records processed:"
        print page_index
        print "\n"

        for index in range(0,10):

                           	google_data_list.append(
                                [
                                	#url
                                    google_urls['items'][index]['link'],

                                    #retrieval date
                                    str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')),

                                    #description
                                    google_urls['items'][index]['snippet'],

                                    #data_file
                                    None,

                                    #published_date
                                    None,

                                    #title
                                    google_urls['items'][index]['title'],

                                    #source_id
                                    1
                                ]
                                                 )
        print '\n'
        print "This is the current list"
    
    return google_data_list

g = google_data(3)
print g
print len(g)


