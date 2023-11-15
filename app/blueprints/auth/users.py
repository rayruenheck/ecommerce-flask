from flask import request, jsonify
from app.model import User
from . import users_bp

@users_bp.post('/register-user')
def register_user():
    content = request.json
    username= content['username']
    email = content['email']
    password= content['password']
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        if existing_user.username == username:
            return jsonify({'message': 'Username Taken, Try Again'}), 400
        else:
            return jsonify({'message': 'Email Taken, Try Again'}), 401
    user = User(email=email, username=username)
    user.password = user.hash_password(password)
    user.add_usertoken()
    user.commit()
    print(user)
    return jsonify([{'message': f'{user.username} Registered'}])

@users_bp.post('/verify-user')
def verify_user():
    content = request.json
    print(content)
    email= content['email']
    password= content['password']
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        response = {"usertoken": user.usertoken, 'username' : user.username, 'id' : user.id}
        return response