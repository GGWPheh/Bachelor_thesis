#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print()
print ("""<link rel= "stylesheet" type= "text/css" href="/TFE/Interface.css" />""")
print("<pre>")
print ("""<body>""")
print ("""<div class="miseenpage">""")
#  Extraction.py
#  
#  Copyright 2020 root <root@Laptop Zehams>
import pymysql
import sys
import os
C=pymysql.connect(host="localhost",user="root",db="GENE",password="yy")
c=C.cursor()

x=''
gene = sys.argv[1]
key = sys.argv[2]
keyword_data = key[:-4]+"data"
keyword_node = key[:-4]+"node"
IMP= ["ISQL-","PMID-","DP  -","TI  -","AB  -","OAB -","FAU -","PL  -","OT  -"]

cmd = """select pmid from """+str(keyword_node)+""" where name = %s"""
nb = c.execute(cmd,(gene))

if nb:
	res, = c.fetchall()
	for t in res:
		allpmid = t.split("'")[1:-1]
		if ',' in allpmid:
			while ',' in allpmid:
				allpmid.remove(',')
		w = t.split("'")[1]
	print("The gene :",gene,"can be found in",len(allpmid),"articles.")
	cgrep = """grep %s /opt/TFEwebsite/clear_human_genome"""%gene
	dc = os.popen(cgrep)
	res=dc.readline()
	res=res.strip().split()[1:]
	for i in res:
		x += i+' '
	print("The aliases detected for this gene :<b><i> %s </b></i>"%x)
	# ~ input()
	for w in allpmid:
		cmd = """select * from """+str(keyword_data)+""" where pmid = %s """
		c.execute(cmd,w)
		res = c.fetchall()
		print("---- ----- ----- ---- ---- ---- ----")
		# ~ for x,y in enumerate(res):
			# ~ print(IMP[x],y)
			
		for elem in res:
			for x,y in enumerate(elem):
				y=str(y)
				nb_loop = len(y)//115 + 1
				for i in range(nb_loop):
					if i == 0:print(IMP[x], end="")
					print(y[i*115:(i+1)*115])			
	
			
			
	
else:
	print("This gene :",gene,"doesn't appear in your database!!")
	
print ("""</div>""")
print ("""</body>""")
print ("""	<footer>
		Mentions legales<br>
		&copy; Copyright <b>DOM - Database Of Mining</b> 2020	<br>
		Projet realise en fin de cycle de bachelier dans le but d'obtenir mon diplome en Bio-Informatiquen. Realise par <strong>Ahmed KANFOUD et Cyril RADERMECKER</strong>.
	</footer>""")
