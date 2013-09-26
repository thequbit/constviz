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
    
I originally used just straight-up sqlalchemy for this project, but had some real trouble with it ... so on the 
recommentation of the very awesome [decause](https://github.com/decause) I went to a [knowledge](https://github.com/FOSSRIT/knowledge) interface.
To install knowledge to use it, do the following:

    > git clone https://github.com/FOSSRIT/knowledge.git
    > cd knowledge
    > python setup.py install
    
Then just run runme.py, and after a little bit of time (there is lots of output so you will know if its still working)
you will get a constitutions sqlite3 database within the same folder as the git repo.
    
    > python runme.py


##Ugh, do I have to run this myself!?##

Nope!  Checkout constitutions.sqlite - it's the full list as of 9/25/2013 of all of the constitutions with their full
html, text, and meta data.
  
##That's it!?##

oh calm down.  More to come on interfacing with nltk data.

    
##What's next!?##

A pretty web interface ... maybe flask?  For now, this is all you get ... pop open your favorite sqlite3 browser and start
banging out query's!
