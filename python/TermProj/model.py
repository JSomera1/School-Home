from data import db
from random import randint 



class Product(db.Model):
    __tablename__ = "products"

    id = db.mapped_column(db.Integer, primary_key=True)
    name = db.mapped_column(db.String)
    price = db.mapped_column(db.DECIMAL(10,2))
    inventory = db.mapped_column(db.Integer, default=0)
    category_id = db.mapped_column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", back_populates="products")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "inventory": self.inventory,
            "quantity": self.category
        }

class Category(db.Model):
    __tablename__ = "categories"

    id=db.mapped_column(db.Integer, primary_key=True)
    name = db.mapped_column(db.String)
    products = db.relationship("Product", back_populates="category")

class Customer(db.Model):
    __tablename__ = "customers"

    id=db.mapped_column(db.Integer, primary_key=True)
    name=db.mapped_column(db.String)
    phone=db.mapped_column(db.String)

    orders = db.relationship("Order", back_populates="customers")

    def Completed(self):
        return [x for x in self.orders if x.completed is not None]

    def pending(self):
        return [x for x in self.orders if x.completed is None]

class Order(db.Model):
    __tablename__ = "orders"

    id = db.mapped_column(db.Integer, primary_key=True)
    created = db.mapped_column(db.DateTime, nullable=False, default=db.func.now())
    completed = db.mapped_column(db.DateTime, nullable=True, default=None)
    amount = db.mapped_column(db.DECIMAL(6, 2), nullable=True, default=None)

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
        for i in self.items:
            if i.quantity > i.product.inventory:
                raise ValueError(f"not enough stock for {i.product.name}")
            i.product.inventory -= i.quantity

        self.completed = db.func.now()
        self.amount = self.estimate()

    def to_dict(self):
        items = db.session.execute(db.select(ProductOrder).where(ProductOrder.order_id == self.id)).scalars()
        return {
            "id": self.id,
            # "complete": db.select(Order).where(Order.completed != None),
            "created":self.created,
            "name": self.customers.name,
            "price": self.estimate(),
            "items": [{
                "inventory": items.products.inventory,
                "name": items.products.name,
                "price": items.products.price,
                "quantity": items.quantity
            } for x in items]
            
        }
        

    
class ProductOrder(db.Model):
    __tablename__ = "items"

    product_id = db.mapped_column(db.ForeignKey("products.id"), primary_key=True)

    order_id = db.mapped_column(db.ForeignKey("orders.id"), primary_key=True)

    quantity = db.mapped_column(db.Integer, nullable=False)

    #
    product = db.relationship("Product")
    orders = db.relationship("Order", back_populates='items')

