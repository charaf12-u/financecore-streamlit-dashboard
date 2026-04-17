import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from utils.logger import log_info, log_error

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# --> connection avec db
DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    log_info("Database engine created successfully")
except Exception as e:
    log_error(f"Database connection failed: {str(e)}")
    raise

def get_engine():
    return engine