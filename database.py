from sqlalchemy import create_engine,text
import os

my_secret = os.environ['CONNECTION_STRING']

engine = create_engine(my_secret)

