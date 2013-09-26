from getconstitutions import getconstitutions

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

    constitutions = getconstitutions()
    report("Loading Constitutions into the Database.")
    for const in constitutions:
        country,webid,title,year_enacted,html,text = const
        constitution = Constitution(country=country,
                                    webid=webid,
                                    title=title,
                                    year_enacted=year_enacted,
                                    html=html,
                                    text=text,
                                   )
        DBSession.add(constitution)
        DBSession.flush()
        transaction.commit()
        report("Successfully Saved '{0}'".format(country))
    print "Application Exiting."
main()
