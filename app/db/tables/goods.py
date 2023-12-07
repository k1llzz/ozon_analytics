from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/ozon')

Base = declarative_base()


class Goods(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    url = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    profit = Column(String(255), nullable=False)
