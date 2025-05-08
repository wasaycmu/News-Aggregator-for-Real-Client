from instagram.client import InstagramAPI
#from lxml import html
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import requests

url = "https://www.instagram.com/quranic_botanic_garden/"
r = requests.get(url)
print r.json()
