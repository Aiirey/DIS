import psycopg2
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

try:
    import db
except ModuleNotFoundError:
    print("Error: Set up database connection in db.py file.")
    with open("db.py", "w") as f:
        f.write("db = \"dbname='pob' user='postgres' password = 'UIS'\"\n")
    import db
conn = psycopg2.connect(db.db)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'Pob.login'

from pob.routes import Pob
app.register_blueprint(Pob)
