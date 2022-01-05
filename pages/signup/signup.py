from flask import Blueprint, render_template

# signup blueprint definition
signup = Blueprint('signup', __name__, static_folder='signup', static_url_path='/static', template_folder='templates')
title = 'Matamim | Sign Up'

# Routes
@signup.route('/signup')
def index():
    return render_template('signup.html',title = title)
