from app import app
from app.forms import AddBeerForm
from flask import render_template, redirect, flash, url_for


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

@app.route('/beers')
def beers():
    return render_template('beers.html', title='All beers', beers=mock_beers)


@app.route('/beers/add', methods=['POST', 'GET'])
def add_beer():
    form = AddBeerForm()
    if form.validate_on_submit():
        new_beer = form.beer.data
        new_brewery = form.brewery.data
        mock_beers.append(new_beer)
        mock_breweries.append(new_brewery)
        flash('{} by {} added to the cellar'.format(new_beer, new_brewery))
        return redirect(url_for(beers))

    return render_template('addBeer.html', title='Add a new beer', form=form)
