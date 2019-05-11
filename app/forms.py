from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddBeerForm(FlaskForm):
    brewery = StringField('Brewery', validators=[DataRequired()])
    beer = StringField('Beer name', validators=[DataRequired()])
    quantity = IntegerField('Number of bottles/cans', default=1)
    submit = SubmitField('Add beer')
