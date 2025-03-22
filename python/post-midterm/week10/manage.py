from db import db, create, drop
from app import app
from models import *
import csv


def import_products():
    dict = {}
    with open ("products.csv", encoding="utf-8") as fp:
        lines = csv.DictReader(fp)
        for i in lines:
            [item, price, amount, category] = i.values()
            if category not in dict:
                dict[category]=[]
            dict[category].append({"name":item, "price":price, "amount":amount})
                



def import_customers():
    pass



if __name__ == "__main__":
    # with app.app_context():
    #     remove_tables()
    #     create_tables()
    import_products()
        
