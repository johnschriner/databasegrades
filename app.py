from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from flask_dance.contrib.google import make_google_blueprint, google
import os


# Initialize Flask
app = Flask(__name__)
app.config.from_object(Config)

# Add google auth
google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_OAUTH_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_OAUTH_CLIENT_SECRET"),
    redirect_url="/login/google/authorized",
    scope=["profile", "email"],
)
app.register_blueprint(google_bp, url_prefix="/login")

# Import db from models and init it here
from models import db, User, DatabaseEntry
db.init_app(app)

# Other extensions
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import routes last
import routes

# TEMP: Run DB migrations at startup on Render
with app.app_context():
    from flask_migrate import upgrade
    upgrade()
