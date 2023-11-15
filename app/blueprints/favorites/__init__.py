from flask import Blueprint

favorite_bp = Blueprint('favorite', __name__)

from app.blueprints.favorites import favorite