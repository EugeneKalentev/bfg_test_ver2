import datetime #<- will be used to set default dates on models
from bfg_test.models.meta import Base  #<- we need to import our sqlalchemy metadata from which model classes will inherit
from sqlalchemy import (
    Column,
    Integer,
    Unicode,     #<- will provide Unicode field
    UnicodeText, #<- will provide Unicode text field
    DateTime,    #<- time abstraction field
)


class Search(Base):
    __tablename__ = 'search'
    id = Column(Integer, primary_key=True)
    dt = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(UnicodeText)
    name = Column(UnicodeText)
    label = Column(UnicodeText)