import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    raw_uri = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    if raw_uri.startswith("postgres://"):
        raw_uri = raw_uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = raw_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
