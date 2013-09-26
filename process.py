from nltk import *

from sqlalchemy import *
from sqlalchemy.orm import (
    sessionmaker,
    )
from sqlalchemy.ext.declarative import declarative_base

import transaction

from models import *

import datetime

DBSession = None

def report(text):
    print "[{0}] {1}".format(datetime.datetime.now(),text)

def genhist(text):
    _tokens = nltk.word_tokenize(text)
    dist = nltk.FreqDist(word.lower() for word in _tokens)
    return dist.items()

def main():
    print "Application Starting."

    uri = 'sqlite:///constitutions.sqlite'
    engine =  create_engine(uri)
    Session = sessionmaker(bind=engine)
    global DBSession
    DBSession = scoped_session(
        sessionmaker(extension=ZopeTransactionExtension()))
    DBSession.configure(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    report("Pulling Constitution Text From Database")
    constitutions = DBSession.query(Constitution).all()
    report("Working on {0} Countries".format(len(constitutions)))
    for constitution in constitutions:
        report("Generating Word Histogram for '{0}'".format(constitution.country))
        words = genhist(constitution.text)
        for _word in words:
            w,f = _word
            word = Word(constitution.id,w,f)
            DBSession.add(word)
        report("Saving Histogram Data to Database")
        DBSession.flush()
        transaction.commit()
    report("{0} Countries Processed Successfully".format(len(constitutions)))
    print "Application Exiting."

main()
