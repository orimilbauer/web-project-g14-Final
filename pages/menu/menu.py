from flask import Blueprint, render_template

# menu blueprint definition
menu = Blueprint('menu', __name__, static_folder='menu', static_url_path='/static', template_folder='templates')
title = 'Matamim | Menu'

# Routes
@menu.route('/menu')
def index():
    return render_template('menu.html',title = title)
