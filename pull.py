import sqlite3
import httplib2
from bs4 import BeautifulSoup
import json
import datetime
import nltk
import re

from downloadpage import downloadpage

def report(text):
    print "[{0}] {1}".format(datetime.datetime.now(),text)

def getinfos(url):
    response = downloadpage(url)
    obj = json.loads(response)
    return obj

def pullconst(consturl,id):
    reponse = downloadpage("{0}{1}".format(consturl,id))
    obj = json.loads(reponse)
    return obj['html']

def gettext(html):
    removelist = ['\n','\t']
    for item in removelist:
        html = html.replace(item,'')
    html = html.encode('ascii','ignore')
    soup = BeautifulSoup(html)
    texts = soup.findAll(text=True)
    textlist = filter(visible,texts)
    visibletext = " ".join(textlist)
    return visibletext

# http://stackoverflow.com/a/1983219/2154772
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

def getconstitutions(idsurl="https://www.constituteproject.org/service/constitutions",
                     consturl="https://www.constituteproject.org/service/html?cons_id=",
                    ):
    constitutions = []
    report("Downloading Country List")
    infos = getinfos(idsurl)
    report("Processing Country List")
    for info in infos:
        country = info['country']
        webid = info['id']
        title = info['title']
        year_enacted = info['year_enacted']
        report("Working on '{0}'".format(country))
        html = pullconst(consturl,webid)
        report("Pulled Constitution Successfully. Processing ...")
        text = gettext(html)
        report("Successfully Processed '{0}'".format(country))
        constitutions.append((country,webid,title,year_enacted,html,text))
        #break
    report("Completed Processing Country List")
    return constitutions

def genhist(text):
    # remove all punctuation before tokenizing
    badwords = ['.',',','/','\\',':',';',"'",'"','[',']','{','}','(',')','!','`','~']
    for badword in badwords
        text = text.replace(badword,'')
    _tokens = nltk.word_tokenize(text)
    dist = nltk.FreqDist(word.lower() for word in _tokens)
    return dist.items()

def main():
    print "Application Starting."

    dbfile = 'constitutions.sqlite'
    con = sqlite3.connect(dbfile)
    
    constitutions = getconstitutions()

    with con:
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS constitutions')
        cur.execute("""CREATE TABLE constitutions( 
                                                  country TEXT,
                                                  title TEXT,
                                                  webid TEXT,
                                                  year_enacted INTEGER,
                                                  html TEXT,
                                                  planetext TEXT)"""
                   )
        cur.execute('DROP TABLE IF EXISTS words')
        cur.execute("""CREATE TABLE words(
                                          country TEXT,
                                          webid TEXT,
                                          word TEXT,
                                          frequency INTEGER)"""
                   )
        for constitution in constitutions:
            country,webid,title,year_enacted,html,text = constitution
            cur.execute('INSERT INTO constitutions VALUES(?,?,?,?,?,?)',
                        (country,
                        title,
                        webid,
                        year_enacted,
                        html,
                        text)
                       )
            report("Generating Word Histogram")
            words = genhist(text)
            report("Saving Word Histogram to Database")
            for word in words:
                w,f = word
                # don't save the word if it isn't at least 4 chars long
                if len(w) > 3:
                    cur.execute('INSERT INTO words VALUES(?,?,?,?)',(country,webid,w,f))
            report("Successfully Processed {0} words".format(len(words)))
    con.close()

    report("{0} Countries Processed Successfully".format(len(constitutions)))
    print "Application Exiting."

main()
