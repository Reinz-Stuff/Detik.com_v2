import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik-populer')
def scrape_code():
    link = 'https://www.detik.com/terpopuler'
    url = requests.get(link)
    soup = BeautifulSoup(url.text, 'html.parser')

    list_news = soup.find(attrs={'class': 'grid-row list-content'})

    title = list_news.findAll(attrs={'class': 'media__title'})
    image = list_news.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images=image)


if __name__ == '__main__':
    app.run(debug=True)
