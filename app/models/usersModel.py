from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    id= db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.Text(100))

    def __init__(self, username):
        self.username = username 

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)