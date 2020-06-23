from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [InputRequired(), Length(min = 4, max = 20)])
    password = PasswordField("Password", validators = [InputRequired(), Length(min = 6, max = 30)])
    remember = BooleanField("Remember me")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min = 4, max = 20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min = 6, max = 30)])
    email = StringField("Email", validators=[InputRequired(), Length(max=60), Email(message="Invalid email")])

# python3 -> from run import app -> db.create_all()