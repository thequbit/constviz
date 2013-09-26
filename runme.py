from getconstitutions import getconstitutions

from sqlalchemy import *
from sqlalchemy.orm import (
    sessionmaker,
    )
from sqlalchemy.ext.declarative import declarative_base

import datetime

engine = create_engine('sqlite:///constitutions.sqlite', echo=True)
Session = sessionmaker(bind=engine)
DBSession = Session()
Base = declarative_base()
Base.metadata.create_all(engine)

def report(text):
    print "[{0}] {1}".format(datetime.datetime.now(),text)

def main():
    print "Application Starting."
    constitutions = getconstitutions()
    report("Loading Constitutions into the Database.")
    for const in constitutions:
        (info,html,text) = const
        constitution = Constitution(country=info['country'],
                                    webid=info['id'],
                                    title=info['title'],
                                    year_enacted=info['year_enacted'],
                                    html=html,
                                    text=text,
                                   )
        DBSession.add(constitution)
        report("Successfully Saved '{0}'".format(info.country))
    print "Application Exiting."
main()
