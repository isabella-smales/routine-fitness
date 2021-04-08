from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, SelectMultipleField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError
 #from models import User

class HomeForm(FlaskForm):
    type_of_routine = SelectField('Choose your Workout', choices = ['Daily Routine', 'Weekly Routine'], validators=[DataRequired()])
    submit = SubmitField('Submit')

class DailyForm(FlaskForm):
    time = SelectField('Workout Length', choices = [ 'Short (30 mins)', 'Medium (1 hour)', 'Long (1 hour 30 mins)'], validators=[DataRequired()])    
    muscle_group = SelectMultipleField('Muscle Group', choices = [('Back', 'BK'), ('Chest', 'CH'), ('Arms', 'AR'), ('Biceps', 'BI'), ('Triceps','TR'), ('Shoulders','SH'), ('Legs', 'LG')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class WeeklyForm(FlaskForm):
    days = SelectField('Choose the number of days', choices = ['2 days', '3 days', '4 days', '6 days'], validators=[DataRequired()]) 
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #def validate_username(self, username):
      #  user = User.query.filter_by(username=username.data).first()
       # if user:
        #    raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
