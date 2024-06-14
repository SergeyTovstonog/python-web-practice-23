"""
Session
"""
from sqlalchemy import create_engine, Integer, String, ForeignKey, select
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship

engine = create_engine('sqlite:///example.db', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str]


class Address(Base):
    __tablename__ = 'addresses'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_email: Mapped[str] = mapped_column('email', String(150), nullable=False, index=True)
    city: Mapped[str]
    user_id: Mapped[str] = mapped_column('user_id', Integer, ForeignKey('users.id'))
    user: Mapped['User'] = relationship(User)


Base.metadata.create_all(engine)


if __name__ == '__main__':

    denis = User()
    denis.fullname = "Denis"
    session.add(denis)
    igor = User(fullname='Igor Omelchenko')
    session.add(igor)
    denis_address = Address(user_email='denisua@gmail.com', city='Kyiv', user=denis)
    session.add(denis_address)
    session.commit()

    stmt = select(User).where(User.id==1)
    u = session.execute(stmt).scalar()
    print(u)
    stmt = select(Address).join(Address.user)
    for row in session.execute(stmt).scalars():
        print(row)
        print(row.Address.id, row.Address.user_email, row.Address.user.fullname)

    # # stmt = select(User)
    # db = [dict(zip(["id", "fullname"], (row.User.id, row.User.fullname))) for row in session.execute(stmt)]
    # print(db)
    #
    # stmt = select(User)
    # db = [dict(zip(["id", "fullname"], (row.id, row.fullname))) for row in session.execute(stmt).scalars().all()]
    # print(db)
    stmt = select(Address.city, Address.id)
    addresses = session.execute(stmt).first()
    print(addresses)
    session.close()
