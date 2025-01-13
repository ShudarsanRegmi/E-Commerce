from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import db

views_bp = Blueprint('views', __name__)


@views_bp.route("/")
@views_bp.route("/home")
def home():
    print("Going to render home")
    return render_template('home.html')


@views_bp.route("/uispecs")
def uispecs():
    return render_template('uispecs.html')