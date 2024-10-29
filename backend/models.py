# models.py
from sqlalchemy import Column, Integer, String
# from backend.database import Base
from database import Base

#テーブルの定義
class Product(Base):
    __tablename__ = "Products"

    PRD_ID = Column(Integer, primary_key=True, index=True)
    CODE = Column(String(13), unique=True, index=True)
    NAME = Column(String(50))
    PRICE = Column(Integer)


