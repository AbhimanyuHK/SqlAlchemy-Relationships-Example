from sqlalchemy import Column, Integer, String

from db_config import DBConfig


class TeamModel(DBConfig.ONE_TO_MANY_DECLARATIVE_BASE):
    """Data model for people."""
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
