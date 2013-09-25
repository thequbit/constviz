import nltk

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    DateTime,
    Boolean,
    Unicode,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Constitution(Base):
    __tablename__ = 'constitutions'
    id = Column(Integer, primary_key=True)
    country = Column(Unicode(64), index=True)
    webid = Column(Unicode(64))
    title = Column(Unicode(64))
    year_enacted = Column(Integer)
    html = Column(Text)
    text = Column(Text)

    def __init__(self,country,webid,title,year_enacted,html,text):
        self.country = country
        self.webid = webid
        self.title = title
        self.year_enacted = year_enacted
        self.html = html
        self.text = text

    def gethist(self):
        _tokens = nltk.word_tokenize(self.text)
        hist = nltk.FreqDist(word.lower() for word in _tokens)
        return hist
