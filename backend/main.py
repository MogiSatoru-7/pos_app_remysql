from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Product
import uvicorn

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

# 商品一覧を取得するエンドポイント
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

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
