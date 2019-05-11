from app import app
from flask import render_template

mock_breweries = [
    'Avery Brewing',
    'Boulevard Brewing Co',
    'Breakside',
    'Deschutes',
    'Firestone Walker',
    'Fort George',
    'Founders',
    'Fremont',
    'Goose Island',
    'New Holland Brewing',
    'Odin Brewing',
    'Postdoc',
    'The lost abbey']

mock_beers = [
    'Plankd aged in rum barrels',
    'Terra Incognita',
    'The Oligarch - Piedmontese',
    'The Oligarch - Maple Oligarch',
    'The dissident',
    'The Abyss']

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Karla'}
    return render_template('index.html', title='Home', user=user)

@app.route('/breweries')
def breweries():
    return render_template('breweries.html', breweries=mock_breweries)


@app.route('/brewery/<name>')
def brewery(name):
    return render_template('brewery.html', title=name, brewery=name, beers=mock_beers)
