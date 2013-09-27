import sqlite3

dbfile = 'constitutions.sqlite'
con = sqlite3.connect(dbfile)

with con:
    cur = con.cursor()
    cur.execute('SELECT wordcount,countrycode,country FROM constitutions ORDER BY wordcount DESC')
    results = cur.fetchall()
con.close()

for wordcount,countrycode,country, in results:
    print "{0} [{1}]: {2}".format(country,countrycode,wordcount)