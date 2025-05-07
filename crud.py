from sqlalchemy.orm import Session
from models import Drink, PriceHistory
from datetime import datetime

def get_all_drinks(db: Session):
    return db.query(Drink).all()

def record_sale(db: Session, drink_id: int):
    drink = db.query(Drink).filter(Drink.id == drink_id).first()
    if drink:
        drink.total_sold += 1
        demand_factor = 0.05
        drink.current_price = round(drink.base_price * (1 + demand_factor * drink.total_sold), 2)
        db.add(PriceHistory(drink_id=drink_id, price=drink.current_price, timestamp=datetime.utcnow()))
        db.commit()
