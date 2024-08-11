from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///example.db")


SESSION = sessionmaker(bind=engine, autoflush=True)

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<People(name={self.name}, age={self.age})>"


Base. metadata.create_all(engine)

session = SESSION()

new_people = People(name="Jojo", age=30)
session.add(new_people)
session.commit()

users = session.query(People).all()
print(users)
