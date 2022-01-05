from flask import Blueprint, render_template

# cart blueprint definition
cart = Blueprint('cart', __name__, static_folder='cart', static_url_path='/static', template_folder='templates')
title ='Matamim | Your Cart'

# Routes
@cart.route('/cart')
def index():
    return render_template('cart.html',title = title)
