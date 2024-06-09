from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, current_user, logout_user, login_required
from pob import bcrypt
from pob.forms import *
from pob.models import *
from pob.regex import *


Pob = Blueprint('Pob', __name__)


@Pob.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Pob.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = create_user(form.username.data)
        if user is not None and bcrypt.check_password_hash(user.password,
                                                           form.password.data):
            user.active = True
            login_user(user, remember=form.remember.data)
            return redirect(url_for('Pob.index'))
        else:
            flash('Forkert brugernavn og/eller password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@Pob.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Pob.login'))


@Pob.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('Pob.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        if create_user(form.username.data) is not None:
            flash('Brugernavn allerede i brug.', 'danger')
        elif not validate_username(form.username.data):
            flash('Brugernavn skal starte med et stort bogstav og må kun '
                  'indeholde bogstaver, tal, bindestreg og underscore.',
                  'danger')
        elif not validate_password(form.password.data):
            flash('Kodeord skal indeholde mindst ét tal og ét specialtegn og '
                  'må ikke indeholde mellemrum.', 'danger')
        else:
            hash_ = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
            insert_user(form.username.data, hash_)
            user = load_user(form.username.data)
            login_user(user)
            return redirect(url_for('Pob.index'))
    return render_template('register.html', title='Opret bruger', form=form)


def warehouse(title, subpage, **params):
    categories = find_all_items_by_category()
    form = SearchForm()
    if form.validate_on_submit():
        search = form.search.data
        if search != '':
            categories = find_items_by_category(search_item_by_any(search))
    return render_template('warehouse.html', subpage=subpage, title=title,
                           categories=categories, form=form, **params)


@Pob.route('/', methods=['GET', 'POST'])
@login_required
def index():
    def suppliers(item_ID):
        suppliers = list(map(
            lambda deliverer: deliverer.suppliername + " (Indkøbspris: " +
                              str(deliverer.supplierprice) + ")",
            create_delivers_by_item_ID(item_ID)))
        return ", ".join(suppliers)
    return warehouse('Oversigt', 'warehouse_index.html',
                     get_suppliers = suppliers)


@Pob.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    add_form = AddForm()
    if request.method == 'POST' and 'submit_add' in request.form:
        for change in add_form.changes:
            item_id = str.removeprefix(change.id, 'changes-')
            change_amount = change.data['change']
            user_adds_item(current_user.id, item_id, change_amount)
        return redirect(url_for('Pob.index'))
    return warehouse('Tilførsel', 'warehouse_add.html', add_form = add_form)


@Pob.route('/history')
@login_required
def history():
    history = create_history()
    return render_template('history.html', title='Historik', history = history)


@Pob.route('/add-item', methods=['GET', 'POST'])
@login_required
def add_item():
    item_form = ItemForm()
    item_form.categories.choices = [(c.ID, c.name)
                                    for c in find_all_categories()]
    item_form.suppliers.choices = [(s.ID, s.name)
                                   for s in find_all_suppliers()]
    if item_form.validate_on_submit():
        insert_item(item_form.name.data, item_form.resaleprice.data,
                    item_form.categories.data)
        insert_delivers(item_form.suppliers.data,
                        create_item(item_form.name.data).ID,
                        item_form.supplierprice.data)
        return redirect(url_for('Pob.index'))
    return render_template('add-item.html', title='Tilføj nyt produkt',
                           item_form = item_form)
