from sqlalchemy import Column, Integer, String
from database import Base

class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    flavor = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
