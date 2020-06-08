from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DBConfig:
    session = None

    ONE_TO_ONE_DECLARATIVE_BASE = declarative_base(metadata=MetaData(schema="one_to_one"))
    ONE_TO_MANY_DECLARATIVE_BASE = declarative_base(metadata=MetaData(schema="one_to_many"))
    MANY_TO_MANY_DECLARATIVE_BASE = declarative_base(metadata=MetaData(schema="many_to_many"))

    def __init__(self):
        self.host = 'localhost'
        self.user = 'postgres'
        self.password = 'root'
        self.data_base = 'relationships'
        self.port = '5432'
        self.URL = 'postgresql://{}:{}@{}:{}/{}'
        self.URL = self.URL.format(self.user, self.password, self.host, self.port, self.data_base)
        self.engine = create_engine(self.URL, encoding='utf8')
        self.engine.connect()

    def connection(self):
        if self.session is None:
            self.session = sessionmaker(bind=self.engine)()
        return self.session
