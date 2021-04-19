from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, SelectMultipleField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError

#Form on main page
class HomeForm(FlaskForm):
    type_of_routine = SelectField('Choose your Workout', choices = ['Daily Routine', 'Weekly Routine'], validators=[DataRequired()])
    submit = SubmitField('Submit')

#Form for Daily Routine
class DailyForm(FlaskForm):
    time = SelectField('Workout Length', choices = [ 'Short (30 mins)', 'Medium (1 hour)', 'Long (1 hour 30 mins)'], validators=[DataRequired()])    
    muscle_group = SelectMultipleField('Muscle Group (Select up to 2 using CTRL)', choices = [('Back', 'Back'), ('Chest', 'Chest'), ('Arms', 'Arms'), ('Biceps', 'Biceps'), ('Triceps','Triceps'), ('Shoulders','Shoulder'), ('Legs', 'Legs')], validators=[DataRequired()])
    submit = SubmitField('Submit')

#Form for Weekly Routine
class WeeklyForm(FlaskForm):
    days = SelectField('Choose the number of days', choices = ['2 days', '3 days', '4 days', '6 days'], validators=[DataRequired()]) 
    submit = SubmitField('Submit')

#Registration Form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

#Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
