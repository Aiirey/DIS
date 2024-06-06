from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FormField, FieldList
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Brugernavn', validators=[DataRequired()])
    password = PasswordField('Kodeord', validators=[DataRequired()])
    remember = BooleanField('Husk mig')
    submit = SubmitField('Log ind')


class RegisterForm(FlaskForm):
    username = StringField('Brugernavn', validators=[DataRequired()])
    password = PasswordField('Kodeord', validators=[DataRequired()])
    submit = SubmitField('Opret bruger')


class SearchForm(FlaskForm):
    search = StringField('Indtast produktnavn, kategori eller leverandør...')
    submit = SubmitField('Søg')


class ChangeForm(FlaskForm):
    change = StringField()

class AddForm(FlaskForm):
    changes = FieldList(FormField(ChangeForm))
    submit_add = SubmitField('Tilfør!')
