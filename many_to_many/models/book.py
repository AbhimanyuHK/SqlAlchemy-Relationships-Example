from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db_config import DBConfig
from many_to_many.models.reader import ReaderModel


class BookModel(DBConfig.MANY_TO_MANY_DECLARATIVE_BASE):
    """Data model for players."""
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)

    reader_id = Column(Integer, ForeignKey(ReaderModel.id), nullable=False)
    reader = relationship(ReaderModel, backref="book", cascade="save-update")
