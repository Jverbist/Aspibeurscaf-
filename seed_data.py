
# seed_data.py
from database import SessionLocal
from models import Drink
import os

db = SessionLocal()

drinks = [
    {"name": "Beer", "base_price": 3.0},
    {"name": "Cola", "base_price": 2.5},
    {"name": "Mojito", "base_price": 5.5},
    {"name": "Whiskey", "base_price": 6.0},
    {"name": "Water", "base_price": 1.5},
]

for d in drinks:
    if not db.query(Drink).filter_by(name=d["name"]).first():
        drink = Drink(
            name=d["name"],
            base_price=d["base_price"],
            current_price=d["base_price"],
            total_sold=0
        )
        db.add(drink)

db.commit()
print("✅ Drinks seeded.")
