from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


'''
method://user:port@host:port/path
https://bcit.ca/cit
mysql://user:password@host:port/database

sqlite:///monday.db
just a database that is in a file on your computer
three slashes for absolute path 
'''
engine = create_engine('sqlite:///monday.db', echo=True)
#trying to use a file called 'monday.db' in the current folder

#session is a class that allows you to connect to a database
Session = sessionmaker(bind=engine)