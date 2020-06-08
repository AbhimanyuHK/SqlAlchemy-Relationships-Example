from db_config import DBConfig
from many_to_many.models.book import BookModel


class BookService:

    def __init__(self):
        self.con = DBConfig().connection()

    def all(self):
        return self.con.query(BookModel).all()

    def save(self, **kwargs):
        try:
            pm = BookModel()
            pm.name = kwargs.get("name")
            pm.author = kwargs.get("author")
            pm.reader_id = kwargs.get("reader_id")
            self.con.add(pm)
            self.con.commit()
            return True
        except Exception as e:
            self.con.rollback()
            raise e
