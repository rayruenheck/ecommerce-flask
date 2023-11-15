from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
CORS(app)

from app.blueprints.auth.users import users_bp
app.register_blueprint(users_bp)

from app.blueprints.cart.cart import cart_bp
app.register_blueprint(cart_bp)

from app.blueprints.favorites.favorite import favorite_bp
app.register_blueprint(favorite_bp)

if __name__ == '__main__':
    app.run(debug=True)