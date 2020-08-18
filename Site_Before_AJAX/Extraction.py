#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print()

print("<pre>")
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
		res, = c.fetchall()
		print("---- ----- ----- ---- ---- ---- ----")
		for x,y in enumerate(res):
			print(IMP[x],y)
else:
	print("This gene :",gene,"doesn't appear in your database!!")
	
