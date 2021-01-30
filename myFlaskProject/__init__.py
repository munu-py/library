from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sqa
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from myFlaskProject.config import Config

# giving path to database
db=sqa()
#instantiate db
bcrypt=Bcrypt()
login_manager=LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    from myFlaskProject.Users.routes import users
    from myFlaskProject.Books.routes import books
    from myFlaskProject.Main.routes import main
    from myFlaskProject.Errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(books)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app