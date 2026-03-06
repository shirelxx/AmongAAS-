from pymongo import MongoClient
from sqlalchemy.orm import sessionmaker
from sql import get_db_engine

engine = get_db_engine()
SessionLocal = sessionmaker(bind=engine)
client = MongoClient("localhost", 27017)