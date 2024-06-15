from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship
from fresh_example.db_config import engine


Base = declarative_base()

# Define a simple User model with additional columns
class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    age: Mapped[int]
    address: Mapped[str]
    phone_number: Mapped[str]
    posts = relationship("Post", back_populates="author")  # Define one-to-many relationship

# Define a simple Post model with a foreign key to User
class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    tag: Mapped[str]

    author: Mapped[User] = relationship("User", back_populates="posts")  # Define many-to-one relationship


# Create the tables in the database
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)