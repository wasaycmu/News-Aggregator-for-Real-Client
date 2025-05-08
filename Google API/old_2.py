import pprint
import urllib
import urllib2
import json

from googleapiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyCek_F0HHjWCB5LhlajKDG-1KgzUCx7ODg")

  res = service.cse().list(
      q="Qur'anic Botanic garden",
      cx='000449499422531286556:exjmwogp3qm',
      num= 10
    ).execute()

  pprint.pprint(res)

if __name__ == '__main__':
  main()