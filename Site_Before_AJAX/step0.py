#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print

import sys
import os
import entrezpy.conduit
import pymysql

keyword = sys.argv[1]
prog = sys.argv[2]
keyfile = "/tmp/%s.txt"%keyword

def check_and_fetch(keyword, prog):
	if prog != "SNP":table = keyword+"_data"
	else: table = keyword
	cmdverif="""show tables;"""
	c.execute(cmdverif)
	res=c.fetchall()
	if res.count((table,)):
		print ("database already exist")
		df=open("/tmp/flag","w")
		df.write("flagi flago")
		df.close()
	
	else :
		w = entrezpy.conduit.Conduit('email')
		get_doc = w.new_pipeline() 
		sid = get_doc.add_search({'db' : 'pubmed', 'term' : keyword , 'rettype' : 'count'})
		get_doc.add_fetch({'db' : 'pubmed','retmode' : 'text', 'rettype' : 'medline'}, dependency=sid)	
		# ~ print (" PUBMED : %s  !! TELECHAREMENT EN COURS !! "%keyword)
		sys.stdout = open(keyfile, 'w')
		analyzer = w.run(get_doc)
		sys.stdout = sys.__stdout__



if prog == "SNP" :
	C=pymysql.connect(host="localhost",user="root",db="SNP",password="yy")
	c=C.cursor()
	check_and_fetch(keyword,prog)
else :
	C=pymysql.connect(host="localhost",user="root",db="GENE",password="yy")
	c=C.cursor()
	check_and_fetch(keyword,prog)

