from sqlalchemy import create_engine, Column, Integer, String, select, and_, or_, func, ForeignKey
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from models import User, Post
from db_config import Session

# Create a Session
with Session() as session:
    # Add some users to the database
    users = [
        User(name="Alice", email="alice@example.com", age=30),
        User(name="Bob", email="bob@example.com", age=25),
        User(name="Charlie", email="charlie@example.com", age=35),
    ]
    session.add_all(users)
    session.commit()

    posts = [
        Post(title="First Post", content="Hello World!", author_id=1),
        Post(title="First Post2", content="Hello World!", author_id=1),
        Post(title="First Post3", content="Hello World!", author_id=1),
        Post(title="First Post4", content="Hello World!", author_id=1),
        Post(title="Second Post5", content="SQLAlchemy is awesome!", author_id=2),
        Post(title="Third Post", content="Python programming tips", author_id=1),
    ]
    session.add_all(posts)
    session.commit()

    # # Demonstrating various query methods
    # print("\nUsing .scalar():")
    # # .scalar() retrieves the first column of the first row
    # single_scalar = session.execute(select(User.email, User.name).where(User.name == "Alice")).scalar()
    # print(single_scalar)
    #
    # print("\nUsing .scalars():")
    # # .scalars() retrieves all values of the first column in the result set
    # all_scalars = session.execute(select(User.name).where(User.name.like("%i%"))).scalars().all()
    # print(all_scalars)
    #
    # print("\nUsing .all():")
    # # .all() retrieves all rows of the query result
    # all_users = session.execute(select(User)).all()
    # print([user.User.name for user in all_users])
    # #
    # print("\nUsing .first():")
    # # .first() retrieves the first row of the query result
    # first_user = session.execute(select(User).where(User.name.like("%asdf%"))).first()
    # print(first_user.User.name if first_user else "No result")

    # print("\nUsing .one():")
    # # .one() retrieves exactly one row of the query result and raises an error if the result count is not exactly one
    # try:
    #     one_user = session.execute(select(User).where(User.name.like("A%"))).one()
    #     print(one_user.User.name)
    # except MultipleResultsFound as e:
    #     print("MultipleResultsFound error:", e)
    # except NoResultFound as e:
    #     print("NoResultFound error:", e)
    #
    # print("\nUsing .scalar_one_or_none():")
    # # # .scalar_one_or_none() retrieves the first column of exactly one row or None if no rows are found
    # # try:
    # #     scalar_one_or_none = session.execute(select(User.name).where(User.name == "Alice")).scalar_one_or_none()
    # #     print(scalar_one_or_none)
    # # except MultipleResultsFound as e:
    # #     print("MultipleResultsFound error:", e)
    #
    # print("\nUsing and_:")
    # and_users = session.execute(select(User).where(and_(User.age >= 25, User.age <= 35))).all()
    # print([user.User.name for user in and_users])
    #
    # print("\nUsing or_:")
    # or_users = session.execute(select(User).where(or_(User.name == "Alice", User.name == "Charlie"))).all()
    # print([user.User.name for user in or_users])
    #
    # # Demonstrating aggregation functions
    # print("\nUsing COUNT():")
    # # Count the number of users
    # user_count = session.execute(select(func.count(User.id))).scalar()
    # print("Number of users:", user_count)
    #
    # print("\nUsing SUM():")
    # # Sum of ages of all users
    # total_age = session.execute(select(func.sum(User.age))).scalar()
    # print("Sum of ages:", total_age)
    #
    # print("\nUsing AVG():")
    # # Average age of users
    # average_age = session.execute(select(func.avg(User.age))).scalar()
    # print("Average age:", average_age)
    #
    # print("\nUsing MIN():")
    # # Minimum age of users
    # min_age = session.execute(select(func.min(User.age))).scalar()
    # print("Minimum age:", min_age)
    #
    # print("\nUsing MAX():")
    # # Maximum age of users
    # max_age = session.execute(select(func.max(User.age))).scalar()
    # print("Maximum age:", max_age)

    #relationship - all posts of the single user
    # users = session.execute(select(User).where(User.name == "Alice")).one()
    # for user in users:
    #     print(user.posts)

    posts = session.execute(select(Post)).all()
    for post in posts:
        print(post.Post.title, post.Post.author.name)