from app import db


class Breweries(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address1 = db.Column(db.String(255), nullable=False)
    address2 = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(25), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(255), nullable=False)
    descript = db.Column(db.Text, nullable=False)
    add_user = db.Column(db.Integer, nullable=False)
    last_mod = db.Column(db.DateTime(), nullable=False)
    #beers = db.relationship('Beer', backref='brewery', lazy='dynamic')

    def __repr__(self):
        return '<Brewery {}>'.format(self.name)


class Beers(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    brewery_id = db.Column(db.Integer, nullable=False)  # , db.ForeignKey('brewery.id'))
    name = db.Column(db.String(255), nullable=False)
    cat_id = db.Column(db.Integer, nullable=False)
    # year = db.Column(db.Integer)
    style_id = db.Column(db.Integer, nullable=False)
    abv = db.Column(db.Float, nullable=False)
    ibu = db.Column(db.Float, nullable=False)
    srm = db.Column(db.Float, nullable=False)
    upc = db.Column(db.Integer, nullable=False)
    filepath = db.Column(db.String(255), nullable=False)
    descript = db.Column(db.Text, nullable=False)
    add_user = db.Column(db.Integer, nullable=False)
    last_mod = db.Column(db.DateTime(), nullable=False)


    def __repr__(self):
        return '<Beer {} {}>'.format(self.year, self.name)
