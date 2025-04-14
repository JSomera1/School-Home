from data import db



class Product(db.Model):
    __tablename__ = "products"

    id = db.mapped_column(db.Integer, primary_key=True)
    name = db.mapped_column(db.String)
    price = db.mapped_column(db.DECIMAL(10,2))
    inventory = db.mapped_column(db.Integer, default=0)
    category_id = db.mapped_column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", back_populates="products")

    def to_json(self):
        return {
            "name": self.name,
            "price": self.price,
            "inventory": self.inventory,

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
        return [x.to_json() for x in self.orders if x.completed is not None]

    def pending(self):
        return [x.to_json() for x in self.orders if x.completed is None]
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone" : self.phone,
            "pending_orders": self.pending(),
            "completed_orders": self.Completed()
        }
        
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

    def to_json(self):
        return {
            "id": self.id,
            "completed": bool(self.completed),
            "completed_date": self.completed,
            "created":self.created,
            "name": self.customers.name,
            "estimated_total": self.estimate(),
            "products": [x.to_json() for x in self.items]
            
        }
        
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
    
