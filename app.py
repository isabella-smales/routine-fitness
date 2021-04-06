from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/exercises.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # Disables modification notifications
db = SQLAlchemy(app)

from models import Back

import random


@app.route('/', methods=['GET'])
def home():
    times = ['Short (30 mins)', 'Medium (1 hour)', 'Long (1 hour 30 mins)']
    muscle_groups = ['Back', 'Chest', 'Arms', 'Legs']
    return render_template('home.html', title='Home Page', times=times, muscle_groups=muscle_groups)


@app.route('/result', methods=['GET', 'POST'])
def result():
    select = request.form.get(times)
    return(str(select))

@app.route('/one_workout')
def one_workout():
    no_of_rows = Back.query.count()
    random_sample = random.sample(range(1, no_of_rows + 1), 5)
    list_of_exercises = []
    for i in random_sample:
        random_exercise = Back.query.get(i)
        list_of_exercises.append(random_exercise.exercise_name)
        one_workout = str(list_of_exercises)[1:-1]
    return render_template('one_workout.html', title='One Workout') + f'{one_workout}' 

