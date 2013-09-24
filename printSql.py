#!/usr/bin/env python 

import sqlite3 as sql
import sys 
import re


    


conn = sql.connect("paper.db")
cursor= conn.cursor()

# get journal abbrevations 
cursor.execute("select * from abbrevs order by abbv")

rows = cursor.fetchall();

for row in rows :
    print "@string{%-15s= %s}" % (row[0], row[1])

# get articles
print 

cursor.execute("select bib from bibs order by key ")

rows = cursor.fetchall();

for row in rows :
    print "%s" % (row[0].encode('utf-8'))


