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
    random_number = random.randrange(1, no_of_rows + 1)
    random_exercise = Back.query.get(random_number)
    return f'{random_exercise.exercise_name}' 