from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

class HomeForm(FlaskForm):
    type_of_routine = SelectField('Choose your Workout', choices = ['Daily Routine', 'Weekly Routine'], validators=[DataRequired()])
    submit = SubmitField('Submit')

class InputForm(FlaskForm):
    time = SelectField('Workout Length', choices = [ 'Short (30 mins)', 'Medium (1 hour)', 'Long (1 hour 30 mins)'], validators=[DataRequired()])    
    muscle_group = SelectMultipleField('Muscle Group', choices = [('Back', 'BK'), ('Chest', 'CH'), ('Arms', 'AR'), ('Biceps', 'BI'), ('Triceps','TR'), ('Shoulders','SH'), ('Legs', 'LG')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class WeeklyForm(FlaskForm):
    days = SelectField('Choose the number of days', choices = ['2 days', '3 days'], validators=[DataRequired()]) 
    submit = SubmitField('Submit')