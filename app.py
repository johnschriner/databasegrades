from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
<<<<<<< HEAD
from flask_migrate import Migrate
=======
>>>>>>> 6d1f5582c6f68a1fd0acf1d3102045c88a3a33e6

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
<<<<<<< HEAD
migrate = Migrate(app, db)
=======
>>>>>>> 6d1f5582c6f68a1fd0acf1d3102045c88a3a33e6
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from models import User, DatabaseEntry  # Ensure models are imported
import routes  # Register routes (you’ll create this)

if __name__ == '__main__':
    app.run(debug=True)
