constviz
========

Visualizations and Statistics generated from the worlds constitutions.

![Country Heat Map by Word Count](https://rawgithub.com/thequbit/constviz/master/wordcount.png)

^ A Country Level Heat Map by Word Count Within Their Constitution


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

If you are interested in actually using this file, you should install sqlite3 (in ubuntu below):

    > sudo apt-get install sqlite3


##Ugh, do I have to run this myself!?##

Nope!  Checkout constitutions.sqlite - it's the full list as of 9/25/2013 of all of the constitutions with their meta
data full html, full text, and word histograms.

    
##What's next!?##

A pretty web interface ... maybe flask?  For now, this is all you get ... pop open your favorite sqlite3 browser and
start banging out query's!


##Some Fun SQL Queries##

You can then do fun queries like:

    > sqlite3 constitutions.sqlite
    SQLite version 3.7.9 2011-11-01 00:52:41
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite>
    
####Counts####
    
    sqlite> select count(webid) from constitutions;
    177
    
    sqlite> select count(distinct webid) from constitutions;
    177
    
    
####First 20 Words in the Histogram Ordered by Frequency####
    
    sqlite> select word,frequency from words where lower(country) = "united_states_of_america" order by frequency desc limit 20;
    shall|306
    states|127
    president|110
    united|86
    state|79
    have|63
    congress|60
    section|55
    such|52
    which|43
    from|41
    office|37
    this|36
    amendment|35
    person|34
    house|33
    other|31
    representatives|30
    article|28
    their|28
    
    sqlite> select word,frequency from words where lower(country) = "afghanistan" order by frequency desc limit 20;
    shall|413
    article|180
    well|116
    with|96
    national|92
    state|83
    provisions|79
    afghanistan|77
    assembly|70
    house|68
    president|67
    this|67
    constitution|61
    court|60
    accordance|59
    members|58
    people|58
    have|41
    supreme|39
    duties|32
    sqlite>


####Number of Words in the Constitution####

    sqlite> select wordcount, country from constitutions order by wordcount desc limit 20;
    96207|India
    63099|Malaysia
    61234|Nigeria
    55857|Pakistan
    55775|Sri_Lanka
    54660|Brazil
    53805|Ecuador
    53053|Papua_New_Guinea
    52511|Ghana
    52478|Zimbabwe
    49398|Uganda
    47208|Saint_Kitts_and_Nevis
    46493|Swaziland
    45937|South_Africa
    45829|Colombia
    44103|Mexico
    43973|Thailand
    43871|Kenya
    43666|Sierra_Leone
    43275|Austria

    sqlite> select wordcount, country from constitutions where lower(country) = "united_states_of_america";
    7636|United_States_of_America
