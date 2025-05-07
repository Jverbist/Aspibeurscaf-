from pydantic import BaseModel
from datetime import datetime

class DrinkBase(BaseModel):
    name: str
    base_price: float

class Drink(DrinkBase):
    id: int
    current_price: float
    total_sold: int

    class Config:
        orm_mode = True

class PricePoint(BaseModel):
    timestamp: datetime
    price: float
