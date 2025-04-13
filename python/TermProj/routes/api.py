from flask import Blueprint, jsonify, request
from data import db
from model import *
from datetime import datetime as dt

api_bp = Blueprint("api", __name__)

@api_bp.route("/test")
def example_api():
    return jsonify(["a", {"example":True, "other":"yes"}, ("value", "123")])

@api_bp.route("/products")
def products():
    all_product = db.session.execute(db.select(Product)).scalars()
    return jsonify([product.to_json() for product in all_product])
    
@api_bp.route("/products/<string:name>", methods=["PUT"])
def products_change(name):
    product = db.session.execute(db.select(Product).where(Product.name == name)).scalar()
    data = request.json
    if not product:
        return "product name does not exist", 404
    if data['inventory'] < 1 or data['price'] < 1:
        return "inventory/price cannot be less than 1", 400
    try:
        product.inventory = data['inventory']
        product.price = data["price"]
        db.session.commit()
        return jsonify(product.to_json())
    except TypeError:
        return "inventory/price cannot be negative", 400
    
@api_bp.route("/products/new/<string:name>", methods=["POST"])
def products_add(name):
    data = request.json
    cat = db.session.execute(db.select(Category).where(Category.name == data['category'])).scalar()
    if not cat:
        cat = Category(name=data['category'])   
    new_product = Product(name=data['name'], price=data['price'], category=cat, inventory=data['inventory'])
    db.session.add(new_product)
    db.session.commit()
    return new_product.to_json()

@api_bp.route("/customers")
def show_customer():
    all_customers = db.session.execute(db.select(Customer)).scalars()
    return jsonify([customers.to_json() for customers in all_customers])

@api_bp.route("/orders")
def orders():
    all_orders = db.session.execute(db.select(Order)).scalars()
    return jsonify([customers.to_json() for customers in all_orders])

@api_bp.route("/orders/<ID>")
def product(ID):
    single = db.session.execute(db.select(Order).where(Order.id == ID)).scalars()
    if not bool(single):
        return {"message": "ID not found"}, 404
    else:
        return jsonify([order.to_json() for order in single])

@api_bp.route("/orders/<ORDER_NUMBER>", methods=["PUT"])
def order_number(ORDER_NUMBER):
    order = db.session.execute(db.select(Order).where(Order.id == ORDER_NUMBER)).scalar()
    data = request.json

    if not order:
        return "order does not exist", 404 
    if data['strategy'] == "adjust":
        for items in order.items:
            if items.quantity > items.product.inventory:
                items.quantity = items.product.inventory
                db.session.commit()

    elif data['strategy'] == "delete":
        for items in order.items:
            if items.quantity > items.product.inventory or items.quantity == 0:
                db.session.delete(items)
                db.session.commit()
        
    
    return jsonify(order.to_json())
    
@api_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    customer = db.session.execute(db.select(Customer).where(Customer.phone == data["customer_phone"])).scalar()
    order = Order(customers=customer, created=dt.now())
    
    if not customer:
        return "customer does not exist", 400
    
    
    
    for item in data['items']:
        check = db.session.execute(db.select(Product).where(Product.name == item[0])).scalar()
        if not check:
            return f"{item[0]} does not exist in the database", 400
        
        elif item[1] < 1:
            return "quantity cannot be negative", 400
        
        
        product = ProductOrder(product=check, quantity=item[1], orders=order)
        db.session.add(product)
    db.session.commit()
    return jsonify(order.to_json())

@api_bp.route("/create", methods=["POST"])
def create():
    return 

@api_bp.route("/read", methods=["GET"])
def read():
    return

@api_bp.route("/update", methods=["PUT"])
def update():
    return 

@api_bp.route("/delete", methods=["DELETE"])
def delete():
    return