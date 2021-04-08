from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app import login

class Chest(db.Model):
    __tablename__ = 'chest'
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String)

class Back(db.Model):
    __tablename__ = 'back'
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String)
    
class Arms(db.Model):
    __tablename__ = 'arms'
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String)
    arm_subgroup = db.Column(db.String)
    
class Legs(db.Model):
    __tablename__ = 'legs'
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String)

class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), index=True, unique=True)
   password_hash = db.Column(db.String(128))

   def __repr__(self):
       return '<User {}>'.format(self.username)    

   def set_password(self, password):
       self.password_hash = generate_password_hash(password)

   def check_password(self, password):
       return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
   return User.query.get(int(id))
