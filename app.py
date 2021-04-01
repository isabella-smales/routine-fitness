from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/exercises.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # Disables modification notifications
db = SQLAlchemy(app)

from models import Back

import random

@app.route('/one_exercise')
def one_exercise():
    no_of_rows = Back.query.count()
    random_sample = random.sample(range(1, no_of_rows + 1), 5)
    list_of_exercises = []
    for i in random_sample:
        random_exercise = Back.query.get(i)
        list_of_exercises.append(random_exercise.exercise_name)
    return f'{list_of_exercises}' 


    