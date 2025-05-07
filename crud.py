from sqlalchemy.orm import Session
from models import Drink, PriceHistory
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

def get_all_drinks(db: Session):
    return db.query(Drink).all()



def round_price(value):
    return float((Decimal(value) * 10).to_integral_value(rounding=ROUND_HALF_UP) / 10)

def record_sale(db: Session, drink_id: int):
    all_drinks = db.query(Drink).all()
    sold_drink = next((d for d in all_drinks if d.id == drink_id), None)

    if sold_drink:
        # Increase sold drink price by 0.10
        sold_drink.total_sold += 1
        sold_drink.current_price = round_price(sold_drink.current_price + 0.10)

        # Decrease all others by 0.10, not below €0.50
        for drink in all_drinks:
            if drink.id != drink_id:
                new_price = round_price(drink.current_price - 0.10)
                drink.current_price = max(new_price, 0.5)

        # Record new price
        db.add(PriceHistory(drink_id=sold_drink.id, price=sold_drink.current_price, timestamp=datetime.utcnow()))
        db.commit()


