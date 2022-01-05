from flask import Blueprint, render_template

# payment blueprint definition
payment = Blueprint('payment', __name__, static_folder='payment', static_url_path='/static', template_folder='templates')
title = 'Matamim | Complete your purchase'

# Routes
@payment.route('/payment')
def index():
    return render_template('payment.html',title = title)
