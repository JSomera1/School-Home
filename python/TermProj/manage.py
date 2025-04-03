from data import db
from model import Product, Customer, Category
import csv
from app import app

def create():
    db.create_all()

def drop():
    db.drop_all()


def create_customers():
    with open('customers.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer = Customer(name=row['name'], phone=row['phone'])
            db.session.add(customer)
            db.session.commit()




def create_products():
    with open('products.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for l in reader:
            [name,price,available,category] = l.values()

            possible_category = db.session.execute(db.select(Category).where(Category.name == category)).scalar()
            if not possible_category:
                cat = Category(name=category)
                db.session.add(cat)


            product = Product(name=name,price=price,inventory=available,category=cat)
            db.session.add(product)
            db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        drop()
        create()
        create_customers()
        create_products()