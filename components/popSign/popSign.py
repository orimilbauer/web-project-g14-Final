from flask import Blueprint, render_template

# popSign blueprint definition
popSign = Blueprint('popSign', __name__, static_folder='static', static_url_path='/popSign', template_folder='templates')
