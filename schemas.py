from pydantic import BaseModel

class DrinkBase(BaseModel):
    name: str
    flavor: str
    stock: int

class DrinkCreate(DrinkBase):
    pass

class Drink(DrinkBase):
    id: int

    class Config:
        orm_mode = True