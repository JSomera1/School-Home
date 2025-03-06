#some commands u may need for the lab

from models import Base
#interaction with database^

'''
.MetaData() > data
.MetaData().create_all 
'''
from db import engine 
Base.metadata.create_all(bind=engine)

from models import Product
p = Product(name="something", price=4.5)
from db import Session
session= Session()
session.add(p) #add object and then push into database like python
session.commit()


#sql statements without expression
from sqlalchemy import select
#start remembering sql commands
select(Product).where(Product.name == "Tim")

#can chain
#limit to 10 results
select(Product).where(Product.price < 5).where(Product.name == "Tim").limit(10)

statement = select(Product)
results = session.execute(statement)

data = results.scalar()
# -> data contains select statement selections 
for prod in data:
    print(prod.name, prod.price, prod.id)
    #not usable again 

#read over and over
data = list(data) #<- listing after reading
