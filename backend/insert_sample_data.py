##使用せず。サンプルデータは一旦MySQLで入力したため。

# # insert_sample_data.py
# import os
# from sqlalchemy import create_engine, text
# from dotenv import load_dotenv

# # .envファイルの読み込み
# load_dotenv()

# # 環境変数からデータベース接続情報を取得
# DB_USERNAME = os.getenv("DB_USERNAME")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# # データベース接続URL
# DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# # エンジンの作成
# engine = create_engine(DATABASE_URL)

# # サンプルデータの挿入
# with engine.begin() as connection:
#     # Tax テーブルへのサンプルデータ挿入
#     connection.execute(text("INSERT INTO Tax (CODE, NAME, PERCENT) VALUES ('10', '消費税', 10.00)"))

#     # Products テーブルへのサンプルデータ挿入
#     connection.execute(text("INSERT INTO Products (CODE, NAME, PRICE) VALUES ('1234567890123', '商品A', 1000)"))
#     connection.execute(text("INSERT INTO Products (CODE, NAME, PRICE) VALUES ('9876543210987', '商品B', 100)"))
#     connection.execute(text("INSERT INTO Products (CODE, NAME, PRICE) VALUES ('1122334455667', '商品C', 1200)"))

#     # Transactions テーブルへのサンプルデータ挿入
#     connection.execute(text("""
#         INSERT INTO Transactions (TRD_ID, DATETIME, EMP_CD, STORE_CD, POS_NO, TOTAL_AMT, TTL_AMT_EX_TAX) 
#         VALUES (1, NOW(), 'EMP001', '99999', '001', 1100, 1000)
#     """))
#     connection.execute(text("""
#         INSERT INTO Transactions (TRD_ID, DATETIME, EMP_CD, STORE_CD, POS_NO, TOTAL_AMT, TTL_AMT_EX_TAX) 
#         VALUES (2, NOW(), 'EMP002', '99998', '002', 2200, 2000)
#     """))

#     # TransactionDetails テーブルへのサンプルデータ挿入
#     connection.execute(text("""
#         INSERT INTO TransactionDetails (TRD_ID, PRD_ID, PRD_CODE, PRD_NAME, PRD_PRICE, TAX_CD) 
#         VALUES (1, 1, '1234567890123', '商品A', 1000, '10')
#     """))
#     connection.execute(text("""
#         INSERT INTO TransactionDetails (TRD_ID, PRD_ID, PRD_CODE, PRD_NAME, PRD_PRICE, TAX_CD) 
#         VALUES (1, 2, '9876543210987', '商品B', 100, '10')
#     """))
#     connection.execute(text("""
#         INSERT INTO TransactionDetails (TRD_ID, PRD_ID, PRD_CODE, PRD_NAME, PRD_PRICE, TAX_CD) 
#         VALUES (2, 1, '1234567890123', '商品A', 1000, '10')
#     """))
#     connection.execute(text("""
#         INSERT INTO TransactionDetails (TRD_ID, PRD_ID, PRD_CODE, PRD_NAME, PRD_PRICE, TAX_CD) 
#         VALUES (2, 3, '1122334455667', '商品C', 1200, '10')
#     """))

#     print("Sample data inserted into all tables.")
