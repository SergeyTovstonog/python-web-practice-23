from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the SQLite database
DATABASE_URL = "sqlite:///queries.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)


# Create a session using the new SQLAlchemy 2.0 syntax
Session = sessionmaker(bind=engine, future=True)
