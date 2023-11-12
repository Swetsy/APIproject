from sqlalchemy.orm import Session
from models import Drink
from schemas import DrinkCreate

def get_all_drinks(db: Session):
    return db.query(Drink).all()

def get_drink(db: Session, drink_id: int):
    return db.query(Drink).filter(Drink.id == drink_id).first()

def delete_drink(db: Session, drink_id: int):
    drink = db.query(Drink).get(drink_id)
    if drink:
        db.delete(drink)
        db.commit()

def create_drink(db: Session, drink: DrinkCreate):
    db_drink = Drink(**drink.dict())
    db.add(db_drink)
    db.commit()
    db.refresh(db_drink)
    return db_drink
