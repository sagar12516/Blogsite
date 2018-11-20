from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from mainsite.models import User
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField("Login")

class RegisterForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match')])
    pass_confirm=PasswordField("Confirm Password",validators=[DataRequired()])
    gender=SelectField(u"Gender",choices=[('1','Male'),('2','Female'),('3','Others')])
    submit=SubmitField("Register")

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already exixts")

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already exists")


class UpdateForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    picture=FileField("Update Your Profile picture",validators=[FileAllowed(['jpg','png'])])
    gender=SelectField(u"Gender",choices=[('1','Male'),('2','Female'),('3','Others')])
    submit=SubmitField("Update")

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already exixts")

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already exists")
