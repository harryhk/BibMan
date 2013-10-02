#!/usr/bin/env python 

import cgi 
from subprocess import check_output

import sqlite3 as sql
import sys 
import re

# parser for paper.bib to create table from bib text 



form = cgi.FieldStorage() 

abbv = form.getvalue('abbv')
full = form.getvalue('full')


e = entry(text)
conn = sql.connect("/home/kun/Research/Bib/database/paper.db")
cursor=conn.cursor()
cursor.execute("INSERT INTO abbrevs VALUES (?,?)", (abbv, full) )

conn.commit()

print "Content-type: text/html"
print 

print '''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<p> Success update </p>
'''

print '<pre>'
print abbv, full

print '</pre>'

print '''
</form>
</body>
</html>
'''
