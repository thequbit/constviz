constviz
========

Visualizations and Statistics generated from the worlds constitutions.

##What is this!?##

After being shown [The Constitute Project](https://www.constituteproject.org) by a friend, I thought there was
just too much data there not to play with.  This is a series of tools to allow you to pull down the data off of the
Constitute Projects website (via very convenient to use API's, thanks!).  Once downloaded, it will use sqlalchemy to place
the meta data about the constitution (country name, year enacted, webid, and title), the raw HTML, as well as the processed
text into a sqlite3 database.


##How do I use this!?##

First, install the dependencies:

    > pip install BeautifulSoup4
    > pip install nltk
    > pip install sqlite3
    
Next, run the pull.py file to pull down the country list, then the constitutions, convert them from html to plain text
then use nltk to produce tokens, and then do a frequency distrobution (histogram) on those words.

    > python pull.py

The output is a rather large sqlite3 database that holds constitution meta data, html, plain text, and word histograms


##Ugh, do I have to run this myself!?##

Nope!  Checkout constitutions.sqlite - it's the full list as of 9/25/2013 of all of the constitutions with their meta
data full html, full text, and word histograms.

    
##What's next!?##

A pretty web interface ... maybe flask?  For now, this is all you get ... pop open your favorite sqlite3 browser and start
banging out query's!
