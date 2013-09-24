#!/usr/bin/env python 

import sqlite3 as sql
import sys 
import re

conn = sql.connect("paper.db")
cursor= conn.cursor()

cursor.execute("""
CREATE TABLE abbrevs (abbv text primary key, term text )
""")

fin = [ i.strip() for i in open(sys.argv[1]) ] 
for i in fin:
    i_temp = re.match(r".*{(.*)=(.*)}", i )
    abv = i_temp.groups(0)[0].strip().lower()
    tem = i_temp.groups(0)[1].strip()
    cursor.execute("INSERT INTO abbrevs VALUES (?,?)", (abv, tem) )

conn.commit()
