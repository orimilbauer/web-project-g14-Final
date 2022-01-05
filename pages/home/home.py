from flask import Blueprint, render_template, redirect, url_for

# home blueprint definition
home = Blueprint('home', __name__, static_folder='home', static_url_path='/static', template_folder='templates')
title = 'Matamim | Home'

# Routes
@home.route('/home')
@home.route('/')
def index():
    return render_template('home.html',title = title)


