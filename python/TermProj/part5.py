from models import Category, Product
from data import db
from app import app
import csv

def create_products():
    with open('final-products.csv', encoding="utf8") as csvfile:
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
    app.app_context().push()
    create_products()
    
