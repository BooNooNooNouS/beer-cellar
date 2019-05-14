from app import app
from app.models import Breweries, Beers
from app.forms import AddBeerForm
from flask import render_template, redirect, flash, url_for

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Karla'}
    return render_template('index.html', title='Home', user=user)

@app.route('/breweries')
def breweries():
    b = Breweries.query.all()
    return render_template('breweries.html', breweries=b)


@app.route('/brewery/<name>')
def brewery(name):
    brewery = Breweries.query.filter_by(name=name).first_or_404()
    return render_template('brewery.html', title=name, brewery=name, beers=[])

@app.route('/beers')
def beers():
    b = Beers.query.all()
    return render_template('beers.html', title='All beers', beers=b[:50])


@app.route('/beers/add', methods=['POST', 'GET'])
def add_beer():
    form = AddBeerForm()
    if form.validate_on_submit():
        new_beer = form.beer.data
        new_brewery = form.brewery.data
        # mock_beers.append(new_beer)
        # mock_breweries.append(new_brewery)
        flash('{} by {} added to the cellar'.format(new_beer, new_brewery))
        return redirect(url_for(beers))

    return render_template('addBeer.html', title='Add a new beer', form=form)
