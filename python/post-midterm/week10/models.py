from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, DECIMAL
from db import db

class Product(db.Model):
    #will have attributes that are stored in the database
    #all fields in the data table 
    __tablename__ = "Products"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    price = mapped_column(DECIMAL(10,2), default=0)
    inventory = mapped_column(Integer, default=0)
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

