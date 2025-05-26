from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

# Initialize Flask
app = Flask(__name__)
app.config.from_object(Config)

# Import db from models and init it here
from models import db, User, DatabaseEntry
db.init_app(app)

# Other extensions
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import routes last
import routes

# Run migrations automatically at startup (TEMPORARY)
with app.app_context():
    from flask_migrate import upgrade
    upgrade()