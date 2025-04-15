from flask import Flask, render_template, url_for, redirect, request
from pathlib import Path
from data import db
from models import Customer, Order, Product, Category, ProductOrder
from routes import api_bp, html_bp, exam_bp


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///t.db"
app.instance_path = Path("change_this").resolve()
db.init_app(app)

app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(html_bp, url_prefix="/html")
app.register_blueprint(exam_bp, url_prefix="/exam")
    

if __name__=="__main__":
    app.run(debug=True, port=3000)