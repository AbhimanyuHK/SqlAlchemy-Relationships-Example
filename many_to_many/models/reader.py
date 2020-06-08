from sqlalchemy import Column, Integer, String

from db_config import DBConfig


class ReaderModel(DBConfig.MANY_TO_MANY_DECLARATIVE_BASE):
    """Data model for players."""
    __tablename__ = "reader"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
