from flask import render_template, url_for, flash, redirect, request, Blueprint
from bank import app, conn, bcrypt
from bank.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from bank.models import Users
from bank import session

Login = Blueprint('Login', __name__)

@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Warehouse.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = Users(1, "John")
        user.active = True
        
        if user != None and True or bcrypt.check_password_hash(user.name_, form.password.data):

            session["id"] = form.username.data

            login_user(user, remember=form.remember.data)
            return redirect(url_for('Warehouse.index'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')

    return render_template('login.html', title='Login', form=form)

@Login.route("/logout")
def logout():
    session["id"]=-1
    logout_user()
    return redirect(url_for('Login.login'))

@Login.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
