#!/usr/bin/env python2
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print

import pymysql
from malib import *
print("<pre>")

	

	
# ~ C=pymysql.connect(host="localhost",user="apache",db="GENE")
# ~ c=C.cursor()
# ~ cmd="""select * from node limit 5"""
	
# ~ c.execute(cmd)
# ~ myresult = c.fetchall()
# ~ print(myresult)
# ~ if not(myresult):
	# ~ print "Votre historique des blats est vide"
	# ~ print "--------------------------------------------------"
	
	

print """<a href="view.cgi"><input type="button" value="Visualiser"></a>"""





f=open("html.html")
print f.read()



