from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FloatField, IntegerField, DateTimeField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, NumberRange
from datetime import datetime
from .constants import STATES_CITY


# User Registration Form
class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=80)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired(), Length(min=5, max=120)])
    state = SelectField('State', choices=[(state, state) for state in STATES_CITY.keys()], validators=[DataRequired()])
    city = SelectField('City', choices=[(None, 'Select a city')], validators=[DataRequired()])
    role = SelectField('Role', choices=[('user', 'User'), ('delivery', 'Delivery')], validators=[DataRequired()])
    pincode = StringField('Pincode', validators=[DataRequired(), Length(min=6, max=10)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


# User Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
