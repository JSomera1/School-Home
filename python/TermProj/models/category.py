from data import db

class Category(db.Model):
    __tablename__ = "categories"

    id=db.mapped_column(db.Integer, primary_key=True)
    name = db.mapped_column(db.String)
    products = db.relationship("Product", back_populates="category")