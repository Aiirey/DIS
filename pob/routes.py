from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from pob import bcrypt
from pob.forms import *
from pob.models import *


Pob = Blueprint('Pob', __name__)


@Pob.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Pob.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = create_user(form.username.data)
        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            user.active = True
            login_user(user, remember=form.remember.data)
            return redirect(url_for('Pob.index'))
        else:
            flash('Forkert brugernavn og/eller password.', 'danger')

    return render_template('login.html', title='Login', form=form)


@Pob.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Pob.login'))


def warehouse(title, subpage):
    categories = find_all_items_by_category()
    form = SearchForm()
    if form.validate_on_submit():
        search = form.search.data
        categories = find_items_by_category(search_item_by_any(search))
    return render_template('warehouse.html', subpage=subpage, title=title,
                           categories=categories, form=form)


@Pob.route("/", methods=['GET', 'POST'])
@login_required
def index():
    return warehouse('Warehouse', 'warehouse_index.html')
