import pdfkit
from google import search

#for url in search('quranic botanic garden', tld='com', stop=1):
pdfkit.from_url('https://www.marhaba.qa/vcu-q-students-win-quranic-botanic-garden-photography-competition/', 'out.pdf')

