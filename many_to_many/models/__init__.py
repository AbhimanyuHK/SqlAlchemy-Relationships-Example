from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from many_to_many.models.reader import ReaderModel
from many_to_many.models.book import BookModel
from db_config import DBConfig

association_table = Table(
    'association',
    DBConfig.MANY_TO_MANY_DECLARATIVE_BASE.metadata,
    Column('reader_id', Integer, ForeignKey(ReaderModel.id)),
    Column('id', Integer, ForeignKey(BookModel.id))
)
