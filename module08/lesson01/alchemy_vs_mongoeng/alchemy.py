from sqlalchemy import create_engine, Column, Integer, String, select, update, delete, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
DATABASE_URL = "postgresql+psycopg2://username:password@localhost/mydatabase"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# Define the base class
Base = declarative_base()

# Define a sample model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    city = Column(String)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine, future=True)

# Create (Add) a new user
with Session() as session:
    new_user = User(name="John Doe", age=30)
    session.add(new_user)
    session.commit()

# Read (Query) all users
with Session() as session:
    users = session.execute(select(User)).scalars().all()
    for user in users:
        print(user.name, user.age)

# Read (Query) specific user by name
with Session() as session:
    specific_user = session.execute(select(User).filter_by(name="John Doe")).scalar_one()
    print(specific_user.name, specific_user.age)

# Update a user's age
with Session() as session:
    session.execute(
        update(User)
        .where(User.name == "John Doe")
        .values(age=31)
    )
    session.commit()

# Delete a user
with Session() as session:
    session.execute(
        delete(User)
        .where(User.name == "John Doe")
    )
    session.commit()

# Search for users by age
with Session() as session:
    users_by_age = session.execute(
        select(User).where(User.age > 25)
    ).scalars().all()
    for user in users_by_age:
        print(user.name, user.age)


with Session() as session:
    # Group by city and count the number of users in each city
    result = session.execute(
        select(User.city, func.count(User.id).label('total_users'), func.avg(User.age).label('average_age'))
        .group_by(User.city)
        .order_by(func.count(User.id).desc())
    ).all()

    for entry in result:
        print(f"City: {entry.city}, Total Users: {entry.total_users}, Average Age: {entry.average_age}")
