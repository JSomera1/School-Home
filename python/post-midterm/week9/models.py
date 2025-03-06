from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy import Integer, String

#cant just use it because there are issues
class Base(DeclarativeBase):
    pass

class Product(Base):
    #will have attributes that are stored in the database
    #all fields in the data table 
    __tablename__ = "Products"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    price = mapped_column(Integer, default=0)
    #getting similar to SQL

    #relationships 
    category = relationship("Category", back_populates="products")

class Customer(Base):
    __tablename__ = "Customers"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    phone = mapped_column(String, default="")

class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")