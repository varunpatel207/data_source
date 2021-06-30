from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_mixins import ActiveRecordMixin, ReprMixin

from twitch import settings

Base = declarative_base()

DATABASE_NAME = settings.DATABASES['default']['NAME']
DB_USERNAME = settings.DATABASES['default']['USER']
DB_PASSWORD = settings.DATABASES['default']['PASSWORD']
DB_HOST = settings.DATABASES['default']['HOST']

SQLALCHEMY_URL = "postgresql+psycopg2://" + DB_USERNAME + ":" + DB_PASSWORD + '@' + DB_HOST + '/' + DATABASE_NAME

print('SQLALCHEMY_URL')
print(SQLALCHEMY_URL)

engine = create_engine(SQLALCHEMY_URL, pool_size=125, max_overflow=150, pool_pre_ping=True)
session = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(engine)


def log(msg):
    print('\n{}\n'.format(msg))


# Used SQLAlchemy Mixin
# we also use ReprMixin which is optional
class BaseModel(Base, ActiveRecordMixin, ReprMixin):
    __abstract__ = True
    __repr__ = ReprMixin.__repr__

    @classmethod
    def get_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    def add_update(self):
        session.add(self)
        session.commit()
        session.flush()
        return self.id

    def add(self):
        session.add(self)
        session.commit()

BaseModel.set_session(session)
