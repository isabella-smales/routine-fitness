from app import db

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