from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/ozon_db')

Base = declarative_base()


class User(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
