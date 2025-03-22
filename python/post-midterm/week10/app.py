from flask import Flask, render_template

from pathlib import Path
from db import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lynn.db"
app.instance_path = Path(".").resolve()
db.init_app(app)




@app.route("/")
def home():

    # url_for("static", filename="style.css")
    return render_template("home.html", name="tim", my_list=["Khoi", "Alex", "Jorge", "Stanley"])



# @app.route("/customers/<int:id>")
# def customer(id):
#     customer = db.session.execute(db.select(Customer).where(Customer.id == id))



if __name__ == "__main__":
    app.run(debug=True, port=8008)


