import urllib
import urllib2
from bs4 import BeautifulSoup
import json
import datetime
import nltk

def report(text):
    print "[{0}] {1}".format(datetime.datetime.now(),text)

def getinfos(url):
    response = urllib2.urlopen(url)
    obj = json.loads(reponse)
    return obj

def pullconst(id):
    response = urllib2.urlopen(url)
    obj = json.loads(reponse)
    return obj.html

def gettext(html):
    removelist = ['\n','\t']
    for item in removelist:
        html = html.replace(item,'')
    soup = BeautifulSoup(html)
    texts = soup.findAll(text=True)
    visibletext = filter(visible,texts)
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
        report("Working on '{0}'".format(const.country))
        html = pullconst(const.id)
        report("Pulled Constitution Successfully. Processing ...")
        text = gettext(html)
        report("Successfully Processed '{0}'".format(const.country))
        constitutions.append((infos,html,words))
    report("Completed Processing Country List")
    return constitutions
