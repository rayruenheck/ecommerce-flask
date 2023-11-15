from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_urlsafe
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    usertoken = db.Column(db.String(250), unique=True)

    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)
    
    def add_usertoken(self):
        setattr(self,'usertoken',token_urlsafe(32))
    
    def get_id(self):
        return str(self.user_id)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

    def commit(self):
        db.session.add(self)
        db.session.commit()

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    usertoken = db.Column(db.String, nullable=False)
    product_category = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def delete_item(self):
        db.session.delete(self)
        db.session.commit()


    def commit(self):
        db.session.add(self)
        db.session.commit()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def commit(self):
        db.session.add(self)
        db.session.commit()

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)
    usertoken = db.Column(db.String, nullable=False)
    product_category = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    def delete_item(self):
        db.session.delete(self)
        db.session.commit()

    def commit(self):
        db.session.add(self)
        db.session.commit()