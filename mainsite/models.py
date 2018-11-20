from mainsite import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask import redirect,url_for


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    email=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))
    gender=db.Column(db.String(64),index=True)
    profile_image=db.Column(db.String(64),nullable=False,default='download.png')
    posts=db.relationship('BlogPost',backref='author',lazy=True)

    def __init__(self,username,email,password,gender):
        self.username=username
        self.email=email
        self.password_hash=generate_password_hash(password)
        self.gender=gender

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username is :{self.username}"



class BlogPost(db.Model):
    user=db.relationship(User)

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title=db.Column(db.String(128),nullable=False)
    text=db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title=title
        self.text=text
        self.user_id=user_id

    def __repr__(self):
        return f"Post Id:{self.id}  Date and time --{self.date} -- {self.title}"
