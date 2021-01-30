from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,RadioField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_login import current_user
from myFlaskProject.models import User




class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email ID',validators=[DataRequired(),Email()])
    address=StringField('Address',validators=[DataRequired(),Length(min=2,max=100)])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=5,max=20)])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    package=RadioField('Select the package', coerce=int,choices=[('1','Silver'),('2','Gold'),('3','Platinum'),('4','None')])
    submit=SubmitField('SignUp')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username already exists.Please choose a different one")

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That emailid already exists.Please choose a different one")

class LoginForm(FlaskForm):
    email=StringField('Email ID',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email ID',validators=[DataRequired(),Email()])
    package = RadioField('Select the package', coerce=int,
                         choices=[('1', 'Silver'), ('2', 'Gold'), ('3', 'Platinum'), ('4', 'None')])
    submit=SubmitField('Update')

    def validate_username(self,username):
        if username.data!=current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username already exists.Please choose a different one")

    def validate_email(self,email):
        if email.data!=current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That emailid already exists.Please choose a different one")