import datetime #<- will be used to set default dates on models
from bfg_test.models.meta import Base  #<- we need to import our sqlalchemy metadata from which model classes will inherit
from sqlalchemy import (
    Column,
    Integer,
    Unicode,     #<- will provide Unicode field
    UnicodeText, #<- will provide Unicode text field
    DateTime,    #<- time abstraction field
)
import re

from webhelpers2.text import urlify #<- will generate slugs
from webhelpers2.date import distance_of_time_in_words #<- human friendly dates

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', str(s))


class Results(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    dt = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(UnicodeText)
    name = Column(UnicodeText)
    slug = Column(UnicodeText)

    def __init__(self, *args, **kwargs):
        super(Results, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Results id: {}, title: {}>'.format(self.id, self.title)

    @property
    def slug(self):
        return urlify(self.title)

    @property
    def created_in_words(self):
        return distance_of_time_in_words(self.created,
                                         datetime.datetime.utcnow())