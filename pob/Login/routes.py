from flask import render_template, url_for, flash, redirect, request, Blueprint
from pob import app, conn, bcrypt
from pob.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from pob.models import Users, create_user
from pob import session

Login = Blueprint('Login', __name__)

@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Warehouse.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = create_user(form.username.data)

        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            user.active = True
            session["id"] = form.username.data

            login_user(user, remember=form.remember.data)
            return redirect(url_for('Warehouse.index'))
        else:
            flash('Forkert brugernavn og/eller password.', 'danger')

    return render_template('login.html', title='Login', form=form)

@Login.route("/logout")
def logout():
    session["id"]=-1
    logout_user()
    return redirect(url_for('Login.login'))
