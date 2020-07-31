from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min = 4, max = 20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min = 6, max = 30)])
    email = StringField("Email", validators=[InputRequired(), Length(max=60), Email(message="Invalid email")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [InputRequired(), Length(min = 4, max = 20)])
    password = PasswordField("Password", validators = [InputRequired(), Length(min = 6, max = 30)])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")

