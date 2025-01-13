from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    form = LoginForm()