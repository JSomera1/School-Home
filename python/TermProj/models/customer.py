from data import db
from .orders import Order 

class Customer(db.Model):
    __tablename__ = "customers"

    id=db.mapped_column(db.Integer, primary_key=True)
    name=db.mapped_column(db.String)
    phone=db.mapped_column(db.String)
    money=db.mapped_column(db.DECIMAL(6,2), default=0)
    status=db.mapped_column(db.String, default="regular")

    orders = db.relationship("Order", back_populates="customers")

    def Completed(self):
        stmt = db.select(Order).where(Order.customers.has(Customer.id == self.id)).order_by(Order.completed.desc())
        result = db.session.execute(stmt).scalars()
        return [x.to_json() for x in result if x.completed]

    def pending(self):
        stmt = db.select(Order).where(Order.customers.has(Customer.id == self.id)).order_by(Order.created.asc())
        result = db.session.execute(stmt).scalars()
        return [x.to_json() for x in result if not x.completed]
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone" : self.phone,
            "Money": self.money,
            "status": self.status,
            "pending_orders": self.pending(),
            "completed_orders": self.Completed()
        }
        