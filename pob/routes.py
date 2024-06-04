from flask import render_template, url_for, flash, redirect, request, Blueprint
from pob import app, conn, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from pob import session
from pob.models import *
from pob.forms import *


Pob = Blueprint('Pob', __name__)


@Pob.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Pob.warehouse'))

    form = LoginForm()

    if form.validate_on_submit():
        user = create_user(form.username.data)

        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            user.active = True
            session["id"] = form.username.data

            login_user(user, remember=form.remember.data)
            return redirect(url_for('Pob.warehouse'))
        else:
            flash('Forkert brugernavn og/eller password.', 'danger')

    return render_template('login.html', title='Login', form=form)


@Pob.route("/logout")
def logout():
    session["id"]=-1
    logout_user()
    return redirect(url_for('Pob.login'))


@Pob.route("/", methods=['GET', 'POST'])
def warehouse():
    if not current_user.is_authenticated:
        return redirect(url_for('Pob.login'))
    warehouse = find_all_items_by_category()
    form = SearchForm()
    if form.validate_on_submit():
        search = form.search.data
        warehouse = find_items_by_category(search_item_by_any(search))
    return render_template('warehouse.html', title='Warehouse', warehouse=warehouse, form=form)