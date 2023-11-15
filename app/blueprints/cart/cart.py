from flask import jsonify, request
from . import cart_bp
from app.model import Cart

@cart_bp.post('/add-cart-item')
def add_cart_item():
    content = request.json
    image=content['image']
    product_category=content['product_category']
    usertoken= content['usertoken']
    product_name = content['product_name']
    price= int(content['price'])
    quantity = int(content['quantity'])
    existing_item = Cart.query.filter_by(usertoken=usertoken, product_name=product_name).first()
    if existing_item:
        return jsonify({'message': 'item already in cart'}), 201
    cart_item = Cart(usertoken=usertoken, product_name=product_name, price=price, quantity=quantity, image=image, product_category=product_category)
    cart_item.commit()
    print(cart_item)
    response = {'usertoken': usertoken, 'product_name' : product_name, 'price' : price, 'quantity' : quantity, 'product_category' : product_category}
    return response

@cart_bp.put('/add-item-quantity')
def add_item_quantity():
    content = request.json
    usertoken=content['usertoken']
    product_name=content['product_name']
    product_category=content['product_category']
    price= int(content['price'])
    quantity = int(content['quantity'])
    image = content['image']
    existing_item = Cart.query.filter_by(usertoken=usertoken, product_name=product_name).first()
    if existing_item:
        existing_item.quantity += 1
        existing_item.price += price
        existing_item.commit()
        print(existing_item)

        response = {'usertoken': usertoken, 'product_name' : product_name, 'price' : price, 'quantity' : quantity, 'image' : image, 'product_category' : product_category}
        return response

@cart_bp.put('/remove-item-quantity')
def remove_item_quantity():
    content = request.json
    usertoken=content['usertoken']
    product_name=content['product_name']
    product_category=content['product_category']
    image = content['image']
    price= int(content['price'])
    quantity = int(content['quantity'])
    existing_item = Cart.query.filter_by(usertoken=usertoken, product_name=product_name).first()
    if existing_item:
        existing_item.quantity -= 1
        existing_item.price -= price
        existing_item.commit()
        print(existing_item)

        response = {'usertoken': usertoken, 'product_name' : product_name, 'price' : price, 'quantity' : quantity, 'image' : image, 'product_category' : product_category}
        return response
    
@cart_bp.get('/get-cart-items')
def get_cart_items():
    result = []
    cart_items = Cart.query.all()
    for item in cart_items:
        result.append({  
            'image' : item.image,    
            'usertoken' : item.usertoken,
            'product_name' : item.product_name,
            'product_category' : item.product_category,
            'price' : item.price,
            'quantity' : item.quantity,
            'id' : item.id
        })
    return jsonify(result), 200

@cart_bp.delete('/get-cart-items/<int:id>')
def delete_cart_item(id):
    cart_item = Cart.query.get(id)
    print(cart_item)
    if cart_item:
        cart_item.delete_item()
        return jsonify({'message': 'Cart item deleted successfully.'}), 200
    else:
        return jsonify({'message': 'Cart item not found.'}), 404