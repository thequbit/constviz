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
    #response = urllib2.urlopen(url)
    #obj = json.loads(reponse)
    #response = requests.get(url)
    #headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36',
    #           'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #           'scheme' : 'https'
    #          }
    #request = urllib2.Request(url, headers=headers)
    #response = urllib2.urlopen(request)
    #obj = json.loads(reponse.read())

    #conn = httplib2.Http(".cache")
    #page = conn.request(url,"GET")
    response = downloadpage(url)
    obj = json.loads(response)
    return obj

def pullconst(consturl,id):
    #response = urllib2.urlopen("{0}{1}".format(consturl,id))
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
        report("Working on '{0}'".format(info['country']))
        html = pullconst(consturl,info['id'])
        report("Pulled Constitution Successfully. Processing ...")
        text = gettext(html)
        report("Successfully Processed '{0}'".format(info['country']))
        constitutions.append((infos,html,text))
    report("Completed Processing Country List")
    return constitutions
