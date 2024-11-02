# create_tables.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# 環境変数からデータベース接続情報を取得
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# データベース接続URL
DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"

# データベース再作成用エンジン
engine = create_engine(DATABASE_URL)

# データベースの再作成
with engine.connect() as connection:
    # データベースが存在する場合は削除
    connection.execute(text(f"DROP DATABASE IF EXISTS {DB_NAME}"))
    print(f"Database {DB_NAME} dropped.")

    # データベースの作成
    connection.execute(text(f"CREATE DATABASE {DB_NAME}"))
    print(f"Database {DB_NAME} created.")

# 再作成したデータベースに接続
engine = create_engine(f"{DATABASE_URL}{DB_NAME}")

# テーブルの作成
with engine.connect() as connection:
    # Productsテーブルの作成
    connection.execute(text("""
        CREATE TABLE Products (
            PRD_ID INT AUTO_INCREMENT PRIMARY KEY,
            CODE CHAR(13) UNIQUE,
            NAME VARCHAR(50),
            PRICE INT
        )
    """))
    print("Table Products created.")

    # Taxテーブルの作成
    connection.execute(text("""
        CREATE TABLE Tax (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            CODE CHAR(2) UNIQUE,
            NAME VARCHAR(20),
            PERCENT DECIMAL(5, 2)
        )
    """))
    print("Table Tax created.")

    # Transactionsテーブルの作成
    connection.execute(text("""
        CREATE TABLE Transactions (
            TRD_ID INT AUTO_INCREMENT PRIMARY KEY,
            DATETIME TIMESTAMP,
            EMP_CD CHAR(10),
            STORE_CD CHAR(5),
            POS_NO CHAR(3),
            TOTAL_AMT INT,
            TTL_AMT_EX_TAX INT
        )
    """))
    print("Table Transactions created.")

    # TransactionDetailsテーブルの作成
    connection.execute(text("""
        CREATE TABLE TransactionDetails (
            TRD_ID INT,
            DTL_ID INT AUTO_INCREMENT PRIMARY KEY,
            PRD_ID INT,
            PRD_CODE CHAR(13),
            PRD_NAME VARCHAR(50),
            PRD_PRICE INT,
            TAX_CD CHAR(2),
            FOREIGN KEY (TRD_ID) REFERENCES Transactions(TRD_ID),
            FOREIGN KEY (PRD_ID) REFERENCES Products(PRD_ID)
        )
    """))
    print("Table TransactionDetails created.")

    # PurchaseHistoryテーブルの作成
    connection.execute(text("""
        CREATE TABLE PurchaseHistory (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_code CHAR(13),
            quantity INT,
            total_price INT,
            purchased_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_code) REFERENCES Products(CODE)
        )
    """))
    print("Table PurchaseHistory created.")

print("All tables created successfully.")
