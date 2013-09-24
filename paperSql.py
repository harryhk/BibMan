#!/usr/bin/env python 

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
    


conn = sql.connect("paper.db")
cursor= conn.cursor()

conn.text_factory = str

cursor.execute("""
CREATE TABLE bibs (key text primary key, title text, authors text, journal text, year integer, bib text   )
""")

fin = [ i for i in open(sys.argv[1]) ] 
idx = [ i for i, j in enumerate(fin) if j[0]=='@' ]
idx.append( len(fin)  )

for i, j  in zip(idx[:-1], idx[1:]):
    e = entry(fin[i:j])
    cursor.execute("INSERT INTO bibs VALUES (?,?,?,?,?,?)", (e.key, e.title, e.author, e.journal, e.year, e.raw ) )


conn.commit()
