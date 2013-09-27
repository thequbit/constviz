
#
# This file based off of the howto here:
# 
# http://www.alexschultz.co.uk/weblog/2010/07/creating-country-level-heatmaps-in-python.html
#
# Thanks Alex Schultz!!!
#

import sqlite3
from bs4 import BeautifulSoup

def main():

    dbfile = 'constitutions.sqlite'
    con = sqlite3.connect(dbfile)

    # get wordcounts from database
    with con:
        cur = con.cursor()
        cur.execute('SELECT wordcount,countrycode FROM constitutions')
        results = cur.fetchall()
    con.close()

    # create dictionary
    worddict = {}
    maxval = 0
    minval = 10000000 # just a big number ...
    for wordcount,countrycode, in results:
        if not countrycode == "":
            worddict[countrycode] = wordcount
            if wordcount > maxval:
                maxval = wordcount
            if wordcount < minval:
                minval = wordcount

    svg = open('countries.svg', 'r').read()

    soup = BeautifulSoup(svg) #, selfClosingTags=['defs','sodipodi:namedview','path'])

    colors = ['#FFF5EB', '#FEE6CE', '#FDD0A2', '#FDAE6B', '#FD8D3C', '#F16913', '#D94801', '#A63603', '#7F2704']

    gs = soup.contents[2].findAll('g',recursive=False)
    paths = soup.contents[2].findAll('path',recursive=False)

    path_style = "fill-opacity:1;stroke:#ffffff;stroke-width:0.99986994;stroke-miterlimit:3.97446823;stroke-dasharray:none;stroke-opacity:1;fill:"

    stepsize = (maxval - minval) / 9

    # replace the style with the color fill you want
    for p in paths:
        if 'land' in p['class']:
            try:
                #rate = penetration[p['id']]
                count = worddict[p['id']]
            except:
                continue
 
            if count > (stepsize * 8):
                color_class = 8
            elif count > (stepsize * 7):
                color_class = 7
            elif count > (stepsize * 6):
                color_class = 6
            elif count > (stepsize * 5):
                color_class = 5
            elif count > (stepsize * 4):
                color_class = 4
            elif count > (stepsize * 3):
                color_class = 3 
            elif count > (stepsize * 2):
                color_class = 2
            elif count > (stepsize * 1):
                color_class = 1
            else:
                color_class = 0
        
            # set the color we are going to use and then update the style
            color = colors[color_class]
            p['style'] = path_style + color


    # now go through all of the groups and update the style
    for g in gs:
        try:
            #rate = penetration[g['id']]
            count = worddict[p['id']]
        except:
            continue
 
       
        if count > (stepsize * 8):
            color_class = 8
        elif count > (stepsize * 7):
            color_class = 7
        elif count > (stepsize * 6):
            color_class = 6
        elif count > (stepsize * 5):
            color_class = 5
        elif count > (stepsize * 4):
            color_class = 4
        elif count > (stepsize * 3):
            color_class = 3
        elif count > (stepsize * 2):
            color_class = 2
        elif count > (stepsize * 1):
            color_class = 1
        else:
            color_class = 0
 
        # set the color we are going to use and then update the style
        color = colors[color_class]
        g['style'] = path_style + color
        # loop through all the paths within this group and update all of their styles too
        for t in g.findAll('path',recursive=True):
            t['style'] = path_style + color


    # write everything out to file
    f = open("wordcount.svg", "w")
    # it's really important that "viewBox" is correctly capitalized and BeautifulSoup kills the capitalization in my tests
    f.write(str(soup).replace('viewbox','viewBox',1))



main()
