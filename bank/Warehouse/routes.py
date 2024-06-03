from flask import render_template, url_for, redirect, Blueprint
from flask_login import current_user
from bank.models import *

Warehouse = Blueprint('Warehouse', __name__)

@Warehouse.route("/", methods=['GET'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('Login.login'))
    warehouse = find_all_items_by_category()
    return render_template('warehouse.html', title='Warehouse', warehouse=warehouse)
