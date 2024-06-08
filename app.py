import os
from flask import Flask
from application.config import LocalDevelopmentConfig
from application.database import db

app = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()
from application.controllers import *

if __name__ == '__main__':
    # Run the Flask app
    app.run()
