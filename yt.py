import urllib.request
import requests
import urllib
from bs4 import BeautifulSoup as bs


url = input('Enter the video URL: ')

cf= urllib.request.urlopen(url)
#print(cf.read())
soup = bs(cf.read(), features='html.parser')

thumb = soup.find('link', {'itemprop': 'thumbnailUrl'})['href']

print('\n Here is the thumbnail:\n')
print(thumb)
print('\n')
input('Press enter to leave...')