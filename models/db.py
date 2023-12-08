import datetime
from sqlalchemy import Column, UUID, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///db.sqlite3")

Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)


class Base(DeclarativeBase):
    __abstract__ = True

    query = db_session.query_property()
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"

class Model(Base):
    __tablename__ = "models"

    id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    size = Column(Integer)

class Scan(Base):
    __tablename__ = "scans"

    id = Column(String, primary_key=True, default=uuid.uuid4)
    model_id = Column(String, ForeignKey("models.id"))

    status = Column(String)
    result = Column(String)


Base.metadata.create_all(engine)
