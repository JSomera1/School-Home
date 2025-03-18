from app import app
from db import db
from sqlalchemy.orm import  mapped_column, relationship
from sqlalchemy import Integer, String
import csv

def create_tables():
    db.create_all(bind=db)

def drop_tables():
    db.drop_all(bind=db)

class Product(db.Model):
    #will have attributes that are stored in the database
    #all fields in the data table 
    __tablename__ = "Products"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    price = mapped_column(Integer, default=0)
    available = mapped_column(Integer, default=0)
    #getting similar to SQL

    #relationships 
    category = relationship("Category", back_populates="products")

class Customer(db.Model):
    __tablename__ = "Customers"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    phone = mapped_column(String, default="")


class Category(db.Model):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")

with open('products.csv') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        prod = Product(name=row['name'], price=row['price'], available=row['available'])
        cat = Category(name=row['category'])
        db.session.add(prod)
        db.session.add(cat)





if __name__ == "__main__":
    with app.app_context():
        drop_tables()
        create_tables()
        db.session.commit()

