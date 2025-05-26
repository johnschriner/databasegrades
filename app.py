from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from models import User, DatabaseEntry  # Ensure models are imported
import routes  # Register routes (you’ll create this)

if __name__ == '__main__':
    app.run(debug=True)
