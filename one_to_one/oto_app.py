from one_to_one.models import DBConfig

db_config = DBConfig()
print("Creating one to one tables")
db_config.ONE_TO_ONE_DECLARATIVE_BASE.metadata.create_all(db_config.engine)
db_config.connection().commit()
