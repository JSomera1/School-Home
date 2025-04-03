from sqlalchemy import String, DECIMAL, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    price = mapped_column(DECIMAL(10,2))
    inventory = mapped_column(Integer, default=0)
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

class Customer(Base):
    __tablename__ = "customers"

    id=mapped_column(Integer, primary_key=True)
    name=mapped_column(String)
    phone=mapped_column(String)

class Category(Base):
    __tablename__ = "categories"

    id=mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")