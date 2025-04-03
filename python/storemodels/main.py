from database import engine, Session
from models import Base, Product, Customer, Category
from sqlalchemy import select
import csv

session=Session()

def create():
    Base.metadata.create_all(engine)

def drop():
    Base.metadata.drop_all(engine)

def create_customers():
    with open("customers.csv", encoding="utf8") as fp:
        lines = csv.DictReader(fp)
        for l in lines:
            [name,phone] = l.values()
            customer = Customer(name=name,phone=phone)
            session.add(customer)
            session.commit()




def create_products():
    with open("products.csv", encoding="utf8") as fp:
        lines = csv.DictReader(fp)
        for l in lines:
            [name,price,available,category] = l.values()
            
            possible_category = session.execute(select(Category).where(Category.name == category)).scalar()
            if not possible_category:
                cat = Category(name=category)
                session.add(cat)
            else:
                cat=possible_category
            
            product = Product(name=name,price=price,inventory=available, category=cat)
            session.add(product)
            session.commit()
