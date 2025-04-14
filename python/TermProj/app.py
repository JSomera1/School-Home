from flask import Flask, render_template, url_for, redirect, request
from pathlib import Path
from data import db
from model import Customer, Order, Product, Category, ProductOrder
from routes import api_bp


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///t.db"
app.instance_path = Path("change_this").resolve()
db.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    sort = request.args.get("sort")

    statement = db.select(Product)

    if sort == "name":
        statement = statement.order_by(Product.name)
    elif sort == "price":
        statement = statement.order_by(Product.price)
    elif sort == "inventory":
        statement = statement.order_by(Product.inventory)
    
    result = db.session.execute(statement).scalars()
    return render_template("products.html", data=result)

@app.route("/categories")
def categories():
    stmt = db.select(Category)
    result = db.session.execute(stmt).scalars()
    return render_template("categories.html", data=result)

@app.route("/categories/<string:name>")
def category_detail(name):
    statement = db.select(Product).where(Product.category.has(Category.name == name))
    cat = db.session.execute(statement).scalars()
    return render_template("category_detail.html", data=cat)

@app.route("/customers")
def customers():
    stmt = db.select(Customer)
    result = db.session.execute(stmt).scalars()
    return render_template("customers.html", customer=result)

@app.route("/customers/<int:id>")
def customers_id(id):
    stmt = db.select(Customer).where(Customer.id == id)
    result = db.session.execute(stmt).scalar()

    return render_template("customers_id.html", data=result)

@app.route("/orders")
def orders():
    sort = request.args.get("sort")

    statement = db.select(Order)

    if sort == "created":
        statement = statement.order_by(Order.created)
    elif sort == "id" or sort == "ID":
        statement = statement.order_by(Order.id)
    elif sort == "amount":
        statement = statement.order_by(Order.amount)
    elif sort == "completed":
        statement = statement.order_by(Order.completed)

    records = db.session.execute(statement).scalars()
    return render_template("orders.html", data=records)

@app.route("/orders/<int:id>")
def order_detail(id):
    statement = db.select(Order).where(Order.id == id)
    order = db.session.execute(statement).scalar()

    if order:
        return render_template("order_detail.html", order=order)
    else:
        return f"No order found with ID {id}", 404

@app.route("/orders/<int:id>/complete", methods=["POST"])
def complete_order(id):
    order = db.session.get(Order, id)
    if not order:
        return f"Order not found", 404
    try:
        order.complete()
        db.session.add(order)
        db.session.commit()
        return redirect(url_for("order_detail", id=id))
    except ValueError as e:
        return render_template("error.html", message=f"{e}"), 409
    
app.register_blueprint(api_bp, url_prefix="/api")
    
    

    


if __name__=="__main__":
    app.run(debug=True, port=3000)