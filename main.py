import requests
from bs4 import BeautifulSoup

urla = 'https://www.detik.com'
urlc = '/terpopuler'

# print('Detik.com - News')
# print('1. Berita populer')
# print('2. Berita Terbaru')
# print('3. Finance')
# print('4. Hot News')
# print('5. Inet')
#
# urlb = input('Pilih berita (1-5): ')
# if urlb == '1':
#     urlc = '/terpopuler'
# elif urlb == '2':
#     urlc = '/terpopuler/news'
# elif urlb == '3':
#     urlc = '/terpopuler/finance'
# elif urlb == '4':
#     urlc = '/terpopuler/hot'
# elif urlb == '5':
#     urlc = '/terpopuler/inet'
#
link = urla + urlc

url = requests.get(link)
soup = BeautifulSoup(url.text, 'html.parser')

list_news = soup.find(attrs={'class': 'grid-row list-content'})

title = list_news.findAll(attrs={'class': 'media__title'})
image = list_news.findAll(attrs={'class': 'media__image'})

for i in image:
    print(i.find('img')['title'])

