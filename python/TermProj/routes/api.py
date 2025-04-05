from flask import Blueprint, jsonify
from data import db
from model import *

api_bp = Blueprint("api", __name__)

@api_bp.route("/test")
def example_api():
    return jsonify(["a", {"example":True, "other":"yes"}, ("value", "123")])

@api_bp.route("/products")
def products():
    all_product = db.session.execute(db.select(Product)).scalars()
    return jsonify([product.to_dict() for product in all_product])

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