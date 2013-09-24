#!/usr/bin/env python 

import cgi 
from subprocess import check_output

print "Content-type: text/html"
print 

print '''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
'''

print '<pre>'

print check_output('/home/kun/Research/Bib/database/printSql.py')

print '</pre>'

print '''
</form>
</body>
</html>
'''
