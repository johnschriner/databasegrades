import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
<<<<<<< HEAD
    raw_uri = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    if raw_uri.startswith("postgres://"):
        raw_uri = raw_uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = raw_uri
=======
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
>>>>>>> 6d1f5582c6f68a1fd0acf1d3102045c88a3a33e6
    SQLALCHEMY_TRACK_MODIFICATIONS = False
