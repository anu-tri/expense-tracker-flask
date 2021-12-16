from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app,db)
    moment.init_app(app)
    cors.init_app(app)


    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.expense import bp as expense_bp
    app.register_blueprint(expense_bp)

    return app
