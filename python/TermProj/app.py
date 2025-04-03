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
    return render_template("home.html")

@app.route("/products")
def products():
    statement = db.select(Product)
    result = db.session.execute(statement).scalars()
    return render_template("products.html", data=result)

@app.route("/products/<string:name>")
def product_detail(name):
    statement = db.select(Product).where(Product.name == name)
    cat = db.session.execute(statement).scalar()
    return render_template("product_detail.html", data=cat)

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/customers")
def customers():
    return render_template("customers.html")




    


if __name__=="__main__":
    app.run(debug=True, port=3000)