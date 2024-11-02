from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Product, PurchaseHistory
from crud import get_product_by_code, add_purchase_history, add_transaction, add_transaction_detail
from pydantic import BaseModel
import uvicorn
from schemas import PurchaseRequest
from datetime import datetime


app = FastAPI()

# CORS設定
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 商品コードで商品情報を取得するエンドポイント
@app.get("/products/{product_code}")
async def fetch_product_by_code(product_code: str, db: Session = Depends(get_db)):
    product = get_product_by_code(db, product_code)
    if not product:
        raise HTTPException(status_code=404, detail="商品が見つかりません")
    return {
        "NAME": product.NAME,
        "PRICE": product.PRICE,
        "PRD_ID": product.PRD_ID,
        "CODE": product.CODE
    }

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

# 購入情報リクエスト用の Pydantic モデル
class PurchaseRequest(BaseModel):
    product_code: str
    quantity: int

# 購入情報を保存するエンドポイント
@app.post("/purchase")
async def purchase_item(request: PurchaseRequest, db: Session = Depends(get_db)):
    # 商品を検索
    product = db.query(Product).filter(Product.CODE == request.product_code).first()
    if not product:
        raise HTTPException(status_code=404, detail="商品が見つかりません")

    # 合計金額を計算
    total_price = product.PRICE * request.quantity

    # `Transactions` テーブルに追加
    transaction_id = add_transaction(db, total_price)

    # `TransactionDetails` テーブルに追加
    add_transaction_detail(db, transaction_id, product, request.quantity)

    # `add_purchase_history` を使って購入履歴を保存
    purchase = add_purchase_history(db, request.product_code, request.quantity, total_price)

    return {
        "transaction_id": transaction_id,
        "product_code": purchase.product_code,
        "quantity": purchase.quantity,
        "total_price": purchase.total_price,
        "purchased_at": purchase.purchased_at
    }

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/")
async def get_items():
    return { "items": ["item1", "item2"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)



# # main.py
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session

# from database import get_db
# from models import Product
# from crud import get_product_by_code
# import uvicorn

# import models
# import database

# # from backend.database import get_db
# # from backend.models import Product
# # from backend.crud import get_product_by_code



# app = FastAPI()

# # CORS設定
# from fastapi.middleware.cors import CORSMiddleware

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 必要に応じて制限
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/products")
# def get_products():
#     print("Accessed /products endpoint")
#     return {"message": "Test"}

# # main.py
# @app.get("/products")
# def get_products(db: Session = Depends(get_db)):
#     try:
#         products = db.query(Product).all()
#         if not products:
#             return {"message": "No products found"}
#         return products
#     except Exception as e:
#         print("Error:", e)
#         return {"error": "Failed to retrieve products"}


# # 商品一覧を取得するエンドポイント
# @app.get("/products")
# def read_products(db: Session = Depends(get_db)):
#     products = db.query(Product).all()
#     return [{"code": product.CODE, "name": product.NAME, "price": product.PRICE} for product in products]

# # 特定の商品を取得するエンドポイント
# @app.get("/products/{code}")
# def read_product(code: str, db: Session = Depends(get_db)):
#     product = get_product_by_code(db, code)
#     if product is None:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return {
#         "code": product.CODE,
#         "name": product.NAME,
#         "price": product.PRICE
#     }




# # main.py
# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from database import get_db
# from models import Product
# import models
# import database


# app = FastAPI()

# # CORS設定
# from fastapi.middleware.cors import CORSMiddleware

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 必要に応じて制限
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # 商品一覧を取得するエンドポイント
# @app.get("/products")
# def get_products(db: Session = Depends(get_db)):
#     products = db.query(Product).all()
#     return products
