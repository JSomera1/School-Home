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