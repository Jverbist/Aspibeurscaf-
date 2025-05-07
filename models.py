from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Drink(Base):
    __tablename__ = "drinks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    base_price = Column(Float)
    current_price = Column(Float)
    min_price = Column(Float, default=0.5)
    total_sold = Column(Integer, default=0)
    history = relationship("PriceHistory", back_populates="drink")

class PriceHistory(Base):
    __tablename__ = "price_history"
    id = Column(Integer, primary_key=True)
    drink_id = Column(Integer, ForeignKey("drinks.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    price = Column(Float)
    drink = relationship("Drink", back_populates="history")
