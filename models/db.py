import datetime
import uuid

from sqlalchemy import (
    Column,
    create_engine,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UUID,
)
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker

engine = create_engine("sqlite:///db.sqlite3")

Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)


class Base(DeclarativeBase):
    __abstract__ = True

    query = db_session.query_property()

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

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
