from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType

from db_config import DBConfig


class ExampleModel(DBConfig.ONE_TO_ONE_DECLARATIVE_BASE):
    """Data model example."""
    __tablename__ = "example_table"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    join_date = Column(DateTime, nullable=False)
    vip = Column(Boolean, nullable=False)
    number = Column(Float, nullable=False)
    data = Column(PickleType, nullable=False)
