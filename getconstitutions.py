#import urllib
#import urllib2
#import requests
from downloadpage import downloadpage
import httplib2
from bs4 import BeautifulSoup
import json
import datetime
import nltk
import re

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
    report("Completed Processing Country List")
    return constitutions
