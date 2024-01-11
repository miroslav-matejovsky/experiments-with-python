import os
from fastapi import FastAPI
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import create_engine

app = FastAPI()
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

@app.get("/")
async def root():
    
    return {
        "message": "Hello World",
        "SQLAlchemy Version": sqlalchemy.__version__
    }