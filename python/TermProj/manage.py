from data import db
from models import Customer, Order, Product, Category, ProductOrder
import csv
from app import app
import random
from datetime import datetime as dt
from datetime import timedelta


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


def random_orders():
    for i in range(15):
        rantime = dt.now() - timedelta(days=random.randint(1,3), hours=random.randint(0,15), minutes=random.randint(0,30))
        random_cus = db.session.execute(db.select(Customer).order_by(db.func.random())).scalar()

        num_prods = random.randint(4,6)
        random_prods = db.session.execute(db.select(Product).order_by(db.func.random()).limit(num_prods)).scalars()

        my_order = Order(customers=random_cus, created=rantime)
        db.session.add(my_order)
        for j in random_prods:
            q = random.randint(1,5)
            name = ProductOrder(product=j, quantity=q, orders=my_order)
            db.session.add(name)
    db.session.commit()
        


if __name__ == "__main__":
    app.app_context().push()
    drop()
    create()
    create_customers()
    create_products()
    random_orders()
    random_orders()
    