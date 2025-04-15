from data import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.mapped_column(db.Integer, primary_key=True)
    created = db.mapped_column(db.DateTime, nullable=False, default=db.func.now())
    completed = db.mapped_column(db.DateTime, nullable=True, default=None)
    amount = db.mapped_column(db.DECIMAL(6, 2), nullable=True, default=None)
    option = db.mapped_column(db.String, default="pickup")

    items = db.relationship("ProductOrder", back_populates='orders')
    customer_id = db.mapped_column(db.Integer, db.ForeignKey("customers.id"))
    customers = db.relationship("Customer", back_populates="orders")  

    def estimate(self):
        total = 0
        for po in self.items:
            one = po.product.price * po.quantity
            total = total + one 
        return total

    def complete(self):
        if self.option == "delivery":
            self.amount + 5
        for i in self.items:
            if i.quantity > i.product.inventory:
                raise ValueError(f"not enough stock for {i.product.name}")
            i.product.inventory -= i.quantity

        self.completed = db.func.now()
        self.amount = self.estimate()

    def to_json(self):
        return {
            "id": self.id,
            "completed": bool(self.completed),
            "completed_date": self.completed,
            "created":self.created,
            "name": self.customers.name,
            "estimated_total": self.estimate(),
            "deliver": bool(self.option), 
            "products": [x.to_json() for x in self.items]
            
        }