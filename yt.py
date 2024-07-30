import urllib.request
import requests
import urllib
from bs4 import BeautifulSoup as bs


url = input('Digite a url do vídeo: ')

cf= urllib.request.urlopen(url)
#print(cf.read())
soup = bs(cf.read(), features='html.parser')

thumb = soup.find('link', {'itemprop': 'thumbnailUrl'})['href']

print('\n Aqui está a thumbnail do vídeo:\n')
print(thumb)
print('\n')
input('Pressione Enter para sair...')