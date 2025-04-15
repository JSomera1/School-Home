from flask import Blueprint, render_template, url_for, redirect, request, jsonify
from data import db
from models import Customer, Order, Product, Category

exam_bp = Blueprint("exam", __name__)

@exam_bp.route("/")
def exam_test():
    return "<h1> hi </h1>"

@exam_bp.route("/customers/<int:id>", methods=["PUT"])
def add_money(id):
    customer = db.session.execute(db.select(Customer).where(Customer.id == id)).scalar()

    data = request.json

    if data["money"] > 1:
        customer.money = data["money"]
    else:
        return "quantity cannot be negative", 400

    if data["premium"] is True:
        customer.status = "premium"
    elif not data["premium"] is True:
        customer.status = "regular"

    db.session.commit()
    return jsonify(customer.to_json())

@exam_bp.route("/order/<int:id>", methods=["PUT"])
def toggle_delivery(id):
    Order = db.session.execute(db.select(Order).where(Order.id == id)).scalar()

    if Order.option == "pickup":
        Order.option = "delivery"
    else:
        Order.option = "pickup"

    db.session.commit()
    return jsonify(Order.to_json())
    