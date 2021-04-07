from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    time = SelectField('Workout length', choices = [ 'Short (30 mins)', 'Medium (1 hour)', 'Long (1 hour 30 mins)'], validators=[DataRequired()])    
    muscle_group = SelectField('Muscle Group', choices = ['Back', 'Chest', 'Arms', 'Legs'], validators=[DataRequired()])
    submit = SubmitField('Submit')
