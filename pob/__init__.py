import psycopg2
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import db


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
#db = "dbname='pob' user='postgres' host='127.0.0.1' password = 'UIS'"
conn = psycopg2.connect(db.db)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'Pob.login'

session = {"id": -1}

from pob.routes import Pob
app.register_blueprint(Pob)
