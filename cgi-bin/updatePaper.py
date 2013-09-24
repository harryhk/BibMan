#!/usr/bin/env python 

import cgi 
from subprocess import check_output

import sqlite3 as sql
import sys 
import re

# parser for paper.bib to create table from bib text 

class entry(object):
    
    def __init__(self, indata):
        # indata starts with @
        # ends with } or empty line 
        self.data=indata
        tmp =  re.match(r".*{(.*),", indata[0])
        self.key = tmp.groups()[0].strip().lower()
        self.raw = ''.join(indata)
        #self.raw = self.raw.encode('utf8')
        self.title, self.author, self.journal, self.year = ('', '', '', '')
        self._parser()
        

    def _parser(self):
        for i in self.data[1:]:
            tmp = re.match(r" *(.*)=", i)
            #index = tmp.groups()[0].strip()
            #value = tmp.groups()[1].strip()
            if tmp:
                index = tmp.groups()[0].strip()
                if index != "journal":
                    tmp = re.match(r".*= *[{\"](.*)[}\"].*", i)
                    value = tmp.groups()[0].strip()
                    if index == "title":
                        self.title = value 
                    if index == "author":
                        self.author = value 
                    if index == "year":
                        self.year = int(value)
                else:
                    tmp = re.match(r".*=(.*),",i)
                    value = tmp.groups()[0].strip()
                    self.journal = value 
    
    def __str__(self):
        #return "(%s) (%s) (%s) " % (self.title, self.author, self.journal) 
        return "(%s) " % (self.raw ) 



form = cgi.FieldStorage() 

text = form.getvalue('bibtex')

# update the database 
text = text.split('\n')

e = entry(text)
conn = sql.connect("/home/kun/Research/Bib/database/paper.db")
cursor=conn.cursor()
cursor.execute("INSERT INTO bibs VALUES (?,?,?,?,?,?)", (e.key, e.title, e.author, e.journal, e.year, e.raw ) )

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
for i  in text:
    print i

print '</pre>'

print '''
</form>
</body>
</html>
'''
