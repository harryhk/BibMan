# BibMan 
I use latex to write scientific papers. However, as my bibtex library grows larger, I feel it become more and more difficult to manage my references. I want to order bibtex by key, to search by authors, year and journal name. Therefore, I create this BibMan. 

BibMan is a bibtex database management program I wrote with sqlite and python. It has an online interface to view and update the database with raw bibtex downloaded from google scholar. 

Right now, it is mostly for my personal use, thus I create it as a minimal version without any error handling or etc.... 


# sqlite Tables
abbrevs

|   abbv     | term          |
| ------------- |-------------|
| Sc      | "Science" |
| Nat      | "Nature"      |

bibs

|   key     | title     |  authors  | journal | year | bib  | 
| ---------|----------|----------|----------|----------|----------|


# Run 
cd currentDirectory
python -m CGIHTTPServer

Then you can go to localhost:8000 and manage your bibtex database 

#Tools included

abbrevSql.py : create database table abbrevs to store journal abbrevations

paperSql.py  : create database table from old bibtex library

printSql.py  : print database into text format so that I can include in latex

index.html   : web interface 

/cgi-bin     : python cgi for online view and update of the database 

