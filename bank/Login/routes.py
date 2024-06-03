from flask import render_template, url_for, flash, redirect, request, Blueprint
from bank import app, conn, bcrypt
from bank.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from bank.models import Users
from bank import session

Login = Blueprint('Login', __name__)

@Login.route("/login", methods=['GET', 'POST'])
def login():

    session["state"]="login"
    role=None

    if current_user.is_authenticated:
        return redirect(url_for('Login.login'))

    form = LoginForm()

    if form.validate_on_submit():

        user = {}
        
        if user != None and bcrypt.check_password_hash(user[2], form.password.data):

            session["id"] = form.id.data

            login_user(user, remember=form.remember.data)
            flash('Login successful.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Login.login'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')

    return render_template('login.html', title='Login', form=form
    , role=role
    )

@Login.route("/logout")
def logout():
    session["id"]=-1
    logout_user()
    return redirect(url_for('Login'))


@Login.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
