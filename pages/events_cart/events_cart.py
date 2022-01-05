from flask import Blueprint, render_template

# events_cart blueprint definition
events_cart = Blueprint('events_cart', __name__, static_folder='events_cart', static_url_path='/static', template_folder='templates')
title = 'Matamim | Events Cart'

# Routes
@events_cart.route('/events_cart')
def index():
    return render_template('events_cart.html',title = title)
