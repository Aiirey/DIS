from flask import render_template, url_for, flash, redirect, request, Blueprint
from bank import app, conn, bcrypt
from flask_login import current_user

import sys, datetime

from bank import session

Warehouse = Blueprint('Warehouse', __name__)

@Warehouse.route("/", methods=['GET'])
def overview():
    if not current_user:
        flash('Please log in.', 'danger')
        return redirect(url_for('Login.login'))
    return render_template('warehouse.html', title='Warehouse')
