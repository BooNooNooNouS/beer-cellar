from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/cellar')
def cellar():
    return "This is a mock of what you have on your cellar, stay tuned"

@app.route('/cellar/breweries')
def breweries():
    return "This is a mock of all the unique breweries you have"

@app.route('/cellar/brewery/<name>')
def brewery(name):
    return "This is a mock of everything we know about brewery " + name