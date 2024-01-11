import os
from fastapi import FastAPI
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

app = FastAPI()
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)

with engine.connect() as connection:
    # result = connection.execute(text("SELECT 1"))
    result = connection.execute(text('SELECT info FROM public."Zoja"'))
    for row in result: 
        print(row)
            
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
 
@app.get("/")
async def root():

    return {
        "message": "Hello World",
        "SQLAlchemy Version": sqlalchemy.__version__
    }