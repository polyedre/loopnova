from flask import Flask

from .extensions import db, migrate
from .routes import main

def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main)

    return app

app = create_app()