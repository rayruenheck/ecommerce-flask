from app.model import Favorite
from flask import jsonify, request
from . import favorite_bp

@favorite_bp.post('/favorite')
def favorite():
    content = request.json
    product_id=content['product_id']
    image=content['image']
    product_category=content['product_category']
    usertoken= content['usertoken']
    product_name = content['product_name']
    price= int(content['price'])
    existing_favorite = Favorite.query.filter_by(usertoken=usertoken, product_name=product_name).first()
    if existing_favorite:
        return jsonify({'message': 'already favorited'}), 201
    favorite_item = Favorite(usertoken=usertoken, product_name=product_name, product_id=product_id, price=price, image=image, product_category=product_category)
    favorite_item.commit()
    print(favorite_item)
    response = {'usertoken': usertoken, 'product_name' : product_name, 'price' : price, 'product_category' : product_category}
    return response

@favorite_bp.get('/get-favorite')
def get_favorite():
    result = []
    favorite_items = Favorite.query.all()
    for item in favorite_items:
        result.append({ 
            'id': item.id, 
            'image' : item.image,    
            'usertoken' : item.usertoken,
            'product_name' : item.product_name,
            'product_category' : item.product_category,
            'price' : item.price,
            'product_id' : item.product_id
        })
    return jsonify(result), 200

@favorite_bp.delete('/get-favorite/<int:product_id>/<string:usertoken>')
def unfavorite(product_id,usertoken):
    favorite_item = Favorite.query.filter_by(product_id=product_id, usertoken=usertoken).first()
    print(favorite_item)
    if favorite_item:
        favorite_item.delete_item()
        return jsonify({'message': 'unfavorited successfully.'}), 200
    else:
        return jsonify({'message': 'favorited item not found.'}), 404