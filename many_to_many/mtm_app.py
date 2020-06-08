from many_to_many.models.book import DBConfig
from many_to_many.service.book_service import BookService
from many_to_many.service.reader_service import ReaderService

db_config = DBConfig()
print("Creating many to many tables")
db_config.MANY_TO_MANY_DECLARATIVE_BASE.metadata.create_all(db_config.engine)
db_config.connection().commit()

reader_data = {
    "name": "Abhimanyu",
}

rs = ReaderService()

rm = rs.get_by_filter(**reader_data)
if rm is None:
    rm = rs.save(**reader_data)

bs = BookService()

for x in range(3):
    book_data = {
        "name": "Geeta {}".format(x),
        "author": "Lord krishna",
        "reader_id": rm.id
    }

    bs.save(**book_data)

for p in bs.all():
    print(p.__dict__, p.reader.__dict__)
