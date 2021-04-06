from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    time = SelectField('Workout length', choices = [ ('Short (30 mins)', 'Short'), ('Medium (1 hour)', 'Medium'), ('Long (1 hour 30 mins)', 'Long') ], validators=[DataRequired()])
    submit = SubmitField('Submit')
