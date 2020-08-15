#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  refreq.py
#  
#  Copyright 2020 root <root@Laptop Zehams & Kydae>
#  
import re
import pymysql
import entrezpy.conduit
import sys
import entrezpy.efetch.efetcher
import os

keyword=sys.argv[1]


C=pymysql.connect(host="localhost",user="root",db="SNP_test",password="yy")
c=C.cursor()

cmdverif="""show tables;"""
c.execute(cmdverif)
res=c.fetchall()
verif_table=[]
for a in res :
	for b in range(len(a)):
		verif_table.append(a[b])

if keyword in verif_table :
	print ("database already exist")

else :
	df = open("/tmp/%s.txt"%keyword,"r")
	text=df.read()
	posPmid=[]
	SNP={}
	verif=0
	pattern = re.compile("PMID- ")
	res = pattern.finditer(text)
	for match in res:
		posPmid.append(match.start()) 
	for i in range(len(posPmid)-1):
		patter = re.compile(r'[ */.:()"\n\'-]rs\d{3,}')
		resu = patter.findall(text, posPmid[i], posPmid[i+1])
		if resu :
			for j in resu :
				cname=j[1:]
				df.seek(posPmid[i])
				x = df.readline()
				x = x.strip().split("- ")[1]
				try :
					SNP[cname].append(x)
				except :
					SNP[cname]=[x]
	L =[]    

	for i in SNP.keys():
		L.append(i[2:])
	keyfile = "/tmp/%s_snp.xml"%keyword
	if not os.path.isfile(keyfile):
		sys.stdout = open("/tmp/%s_snp.xml"%keyword, 'w')
		e = entrezpy.efetch.efetcher.Efetcher('efetcher','email')
		a = e.inquire({'db' : 'snp','id' : L,'retmode' : 'xml', 'rettype' : 'docset' })
	else:
		print("SNP file Found")


"""create table data(
    id INT AUTO_INCREMENT PRIMARY KEY,
    snpid varchar(25))
    engine=MyISAM;"""
    
