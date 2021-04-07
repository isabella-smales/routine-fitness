from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import InputForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/exercises.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # Disables modification notifications
app.config['SECRET_KEY'] = 'string'
db = SQLAlchemy(app)

from models import Back, Chest, Arms, Legs

import random

@app.route('/', methods=['GET','POST'])
def home():
    form = InputForm()
    if not form.validate_on_submit():
        return render_template('home.html', form=form)
    time = form.time.data

    muscle_group = form.muscle_group.data
    muscle1 = muscle_group[0]
    if len(muscle_group) != 1:
        muscle2 = muscle_group[1]
    else:
        muscle2 = muscle1

    if request.method == "POST":
        return redirect(url_for("one_workout", time=time, muscle1=muscle1, muscle2=muscle2))
    else: 
        return render_template("home.html")
    
@app.route("/<time>/<muscle1>/<muscle2>")
def one_workout(time, muscle1, muscle2):
    if time == 'Short (30 mins)':
        no_of_exercises = 4
    elif time == 'Medium (1 hour)':
        no_of_exercises = 6
    elif time == 'Long (1 hour 30 mins)':
        no_of_exercises = 8
    
    list_of_exercises = []

    if muscle2 == muscle1:
        list = [muscle1]
    else:
        list = [muscle1, muscle2]
    for muscle in list:
        if len(list) == 1:
            no_of_rows = eval(muscle).query.count()
            random_sample = random.sample(range(1, no_of_rows + 1), min(no_of_exercises, no_of_rows))
        else:
            no_of_rows = eval(muscle).query.count()
            random_sample = random.sample(range(1, no_of_rows + 1), min(int(no_of_exercises/2), no_of_rows))
        for i in random_sample:
            random_exercise = eval(muscle).query.get(i)
            list_of_exercises.append(random_exercise.exercise_name)
            one_workout = str(list_of_exercises)[1:-1]
    
    return render_template('one_workout.html', title='One Workout') + f'{one_workout}' + f"<h1>{time}</h1>"

