from flask import Flask, render_template
from pathlib import Path
from data import db
from model import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///t.db"
app.instance_path = Path("change_this").resolve()
db.init_app(app)

@app.route("/")
def home():
    return render_template("home.html", my_list=["jian","jorge","alex"])

@app.route("/categories/<string:name>")
def category_detail(name):
    stmt1 = db.select(Category).where(Category.name == name)
    results = db.session.execute(stmt1).scalar()
    return render_template("categories_details.html", category=results)

@app.route("/customers")
def customers():
    statement = db.select(Customer)
    results = db.session.execute(statement).scalars()
    return render_template("customers.html", data=results)

@app.route("/customers/<int:customer_id>")
def customer_detail(customer_id):
    statement = db.select(Customer).where(Customer.id == customer_id)
    results = db.session.execute(statement).scalar()
    return render_template("customer_detail.html", customer=results)

@app.route("/products")
def products():
    statement = db.select(Product)
    results = db.session.execute(statement).scalars()
 
    return render_template("products.html", data=results)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
   
    statement = db.select(Product).where(Product.id == product_id)
    results = db.session.execute(statement).scalar()
    return render_template("product_detail.html", product=results)





    


if __name__=="__main__":
    app.run(debug=True, port=3000)