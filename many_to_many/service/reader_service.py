from db_config import DBConfig
from many_to_many.models.reader import ReaderModel


class ReaderService:

    def __init__(self):
        self.con = DBConfig().connection()

    def all(self):
        return self.con.query(ReaderModel).all()

    def save(self, **kwargs):
        try:
            rm = ReaderModel()
            rm.name = kwargs.get("name")
            self.con.add(rm)
            self.con.commit()
            return rm
        except Exception as e:
            self.con.rollback()
            raise e

    def get_by_filter(self, name):
        return self.con.query(ReaderModel).filter(ReaderModel.name == name).first()
