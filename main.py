import os.path

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from crud import get_all_drinks, get_drink, delete_drink, create_drink
from database import engine, SessionLocal
app = FastAPI()

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/drinks", response_model=list[schemas.Drink])
def read_all_drinks(db: Session = Depends(get_db)):
    return get_all_drinks(db)

@app.get("/drinks/{drink_id}", response_model=schemas.Drink)
def read_drink(drink_id: int, db: Session = Depends(get_db)):
    return get_drink(db, drink_id)

@app.delete("/drinks/{drink_id}")
def delete_drink_endpoint(drink_id: int, db: Session = Depends(get_db)):
    delete_drink(db, drink_id)
    return {"message": "The prime drink is deleted!"}

@app.post("/drinks", response_model=schemas.Drink)
def create_drink_endpoint(drink: schemas.DrinkCreate, db: Session = Depends(get_db)):
    return create_drink(db, drink)
