import os

import psycopg2 as psy
from contextlib import contextmanager

from dotenv import load_dotenv

load_dotenv()

# Database connection parameters
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

@contextmanager
def get_db_connection():
    conn = psy.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    try:
        yield conn
    finally:
        conn.rollback()
        conn.close()
