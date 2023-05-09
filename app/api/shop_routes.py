from . import api
from ..models import Product, Cart
from ..apiauthhelper import token_auth
from flask import request


@api.get('/products')
def getProductsAPI(): 
    products = Product.query.all()
    return {
        'status':'ok',
        'results': len(products),
        'products': [p.to_dict() for p in products]
    }

@api.get('/cart')
@token_auth.login_required
def getCartAPI():
    user = token_auth.current_user()
    return {
        'status': 'ok',
        'cart': [Product.query.get(c.product_id).to_dict() for c in Cart.query.filter_by(user_id=user.id).all()]
    }
    
@api.post('/cart')
@token_auth.login_required
def addToCartAPI():
    user = token_auth.current_user()
    data = request.json

    product_id = data['product_id']
    product = Product.query.get(product_id)

    if product:

        cart_item = Cart(user.id, product.id)
        cart_item.saveToDB()

        return {
            'status': 'ok',
            'message': f'Succesfully added {product.product_name} to your cart!'
        }
    else:
        return {
            'status': 'not ok',
            'message': 'That product does not exist!'
        }
    
@api.delete('/cart/<int:product_id>')
@token_auth.login_required
def removeFromCartAPI(product_id):
    user = token_auth.current_user()
    product = Product.query.get(product_id)
    item = Cart.query.filter_by(user_id=user.id).filter_by(product_id=product_id).first()
    if item:
        item.deleteFromDB()
        return {
            'status': 'ok',
            'message': f"Successfully removed {product.product_name} from cart."
        }
    return {
            'status': 'not ok',
            'message': f"You do not have that item in your cart."
        }