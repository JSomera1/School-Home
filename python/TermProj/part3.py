from models import Customer
from data import db
from app import app

def make():
    names = [["Jian Somera", "604-720-3851"], ["Tim Guicherd", "666-888-9999"]]
    for i in range(len(names)):
        result = db.session.execute(db.select(Customer).where(Customer.name == names[i][0])).scalar()
        if not result:
            customer = Customer(name=names[i][0], phone=names[i][1])
            db.session.add(customer)
    db.session.commit()

if __name__ == "__main__":
    app.app_context().push()
    make()
