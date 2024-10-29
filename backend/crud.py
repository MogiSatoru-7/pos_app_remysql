# crud.py
from sqlalchemy.orm import Session
from models import Product  

def get_product_by_code(db: Session, code: str):
    return db.query(Product).filter(Product.CODE == code).first()
