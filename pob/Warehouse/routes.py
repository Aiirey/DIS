from flask import render_template, url_for, redirect, Blueprint
from flask_login import current_user
from pob.models import *
from pob.forms import *

Warehouse = Blueprint('Warehouse', __name__)

@Warehouse.route("/", methods=['GET', 'POST'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('Login.login'))
    warehouse = find_all_items_by_category()
    form = SearchForm()
    if form.validate_on_submit():
        search = form.search.data
        warehouse = find_items_by_category(search_item_by_any(search))
    return render_template('warehouse.html', title='Warehouse', warehouse=warehouse, form=form)
