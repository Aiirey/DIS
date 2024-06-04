from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Brugernavn', validators=[DataRequired()])
    password = PasswordField('Kodeord', validators=[DataRequired()])
    remember = BooleanField('Husk mig')
    submit = SubmitField('Log ind')

class SearchForm(FlaskForm):
    search = StringField('Indtast produktnavn, kategori eller leverandør...', validators=[DataRequired()])
    submit = SubmitField('Søg')
