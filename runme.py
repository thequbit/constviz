from getconstitutions import getconstitutions

#from sqlalchemy import *
#from sqlalchemy.orm import (
#    sessionmaker,
#    )
#from sqlalchemy.ext.declarative import declarative_base

#import transaction

#from models import *

import datetime

#DBSession = None

from sqlalchemy import create_engine
from knowledge.model import setup_knowledge
from knowledge.model import Entity

def report(text):
    print "[{0}] {1}".format(datetime.datetime.now(),text)

def main():
    print "Application Starting."

    uri = 'sqlite:///constitutions.sqlite'
    #engine =  create_engine(uri)
    #Session = sessionmaker(bind=engine)
    #global DBSession
    #DBSession = scoped_session(
    #    sessionmaker(extension=ZopeTransactionExtension()))
    #DBSession.configure(bind=engine)
    #Base.metadata.create_all(bind=engine)

    #
    # knowlege based approach
    # 
    DBSession = setup_knowledge(uri)

    constitutions = getconstitutions()
    report("Loading Constitutions into the Database.")
    constitution = Entity(u'Constitution')
    for c in constitutions:
        #country,webid,title,year_enacted,html,text = const
        #constitution = Constitution(country=country,
        #                            webid=webid,
        #                            title=title,
        #                            year_enacted=year_enacted,
        #                            html=html,
        #                            text=text,
        #                           )
        #DBSession.add(constitution)
        #DBSession.flush()
        #transaction.commit()


        #
        # FOSS@RIT Knowledge ftw
        #
        country,webid,title,year_enacted,html,text = c
        report("Saving the Constitution of '{0}' to the Database".format(country))
        constitution[u'country'] = country
        constitution[u'webid'] = webid
        constitution[u'title'] = title
        constitution[u'year_enacted'] = year_enacted
        constitution[u'html'] = html
        constitution[u'text'] = text
        DBSession.add(constitution)
        DBSession.commit()
        
        results = DBSession.query(constitution).filter(constitution[u'country'] == country).all()
        for result in results:
            print result['country']
        return
        report("Generating Word Histogram for '{0}'".format(constitution.country))
        words = genhist(constitution.text)
        for _word in words:
            w,f = _word
            word = Entity[u'Word']
            word['id'] = cid

            DBSession.add(word)
        report("Processing Complete for '{0}'".format(country))

    report("Pulling Constitution Text From Database")
    constitutions = DBSession.query(Constitution).all()
    report("Working on {0} Countries".format(len(constitutions)))
    for constitution in constitutions:
        report("Generating Word Histogram for '{0}'".format(constitution.country))
        words = genhist(constitution.text)
        cid = constitution.id
        for _word in words:
            w,f = _word
            word = Word(cid,w,f)
            DBSession.add(word)
            DBSession.flush()
            transaction.commit()
        report("Saving {0} Histogram Data to Database".format(constitution.country))
        #DBSession.flush()
        #transaction.commit()
    report("{0} Countries Processed Successfully".format(len(constitutions)))

    print "Application Exiting."
main()
