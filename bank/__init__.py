from bank import user
from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# TODO: Clean up all imports in all file


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
#db = "dbname='bank' user='postgres' host='127.0.0.1' password = 'UIS'"
conn = psycopg2.connect(user.db)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

session = {"id": 0}

from bank.Login.routes import Login
from bank.Warehouse.routes import Warehouse

app.register_blueprint(Login)
app.register_blueprint(Warehouse)
