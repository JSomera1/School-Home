from data import db


class ProductOrder(db.Model):
    __tablename__ = "items"

    product_id = db.mapped_column(db.ForeignKey("products.id"), primary_key=True)

    order_id = db.mapped_column(db.ForeignKey("orders.id"), primary_key=True)

    quantity = db.mapped_column(db.Integer, nullable=False)

    product = db.relationship("Product")
    orders = db.relationship("Order", back_populates='items')

    def to_json(self):
        return {
            "name": self.product.name,
            "price": self.product.price,
            "inventory": self.product.inventory,
            "quantity": self.quantity
        }
    
