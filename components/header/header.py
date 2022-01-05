from flask import Blueprint, render_template

# header blueprint definition
header = Blueprint('header', __name__, static_folder='header', static_url_path='/static', template_folder='templates')
