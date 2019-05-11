from app import db


class Brewery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    beers = db.relationship('Beer', backref='brewery', lazy='dynamic')

    def __repr__(self):
        return '<Brewery {}>'.format(self.name)

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    year = db.Column(db.Integer)
    style = db.Column(db.String())
    brewery_id = db.Column(db.Integer, db.ForeignKey('brewery.id'))

    def __repr__(self):
        return '<Beer {} {}>'.format(self.year, self.name)
