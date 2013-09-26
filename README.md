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

All you need to do is run the runme.py file, after installing the dependencies:

    > pip install BeautifulSoup4
    > pip install nltk
    > pip install sqlalchemy
    > pip install zope.sqlalchemy
    
Then just run runme.py, and after a little bit of time (there is lots of output so you will know if its still working)
you will get a constitutions sqlite3 database within the same folder as the git repo.
    
    > python runme.py
  
  
##That's it!?##

oh calm down.  More to come on interfacing with nltk data.

    
##What's next!?##

A pretty web interface ... maybe flask?  For now, this is all you get ... pop open your favorite sqlite3 browser and start
banging out query's!
