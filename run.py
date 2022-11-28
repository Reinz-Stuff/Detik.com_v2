import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik-populer')
def detik_populer():
    link = 'https://www.detik.com/terpopuler'
    url = requests.get(link)
    soup = BeautifulSoup(url.text, 'html.parser')

    list_news = soup.find(attrs={'class': 'grid-row list-content'})

    title = list_news.findAll(attrs={'class': 'media__title'})
    image = list_news.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images=image)


@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('index.html', datas=json_data.value())


if __name__ == '__main__':
    app.run(debug=True)
