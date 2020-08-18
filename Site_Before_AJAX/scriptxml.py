#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import re
import pymysql
import entrezpy.conduit
import sys 
import re
from xml.dom import minidom

C=pymysql.connect(host="localhost",user="root",db="SNP",password="yy")
c=C.cursor()

keyword=sys.argv[1]

cmdverif="""show tables;"""
c.execute(cmdverif)
res=c.fetchall()

if res.count((keyword,)) :
	print ("database already exist")

else:
	IMP= ['SPDI','GENES','CHRPOS ']
	data={}
	inutile=0
	L=[]

	mydoc=minidom.parse('/tmp/%s_snp.xml'%keyword)
	items = mydoc.getElementsByTagName('DocumentSummary')
	for z in range(len(items)) :
		for y in range(len(items[z].childNodes)):
				for o in IMP :
					if o in str(items[z].childNodes[y]) and "benign" not in str(items[z].childNodes[6].firstChild):
						if o == 'GENES' :
							L=[]
							for a in range(len(items[z].childNodes[y].childNodes)):
								L.append(items[z].childNodes[y].childNodes[a].firstChild.firstChild.data)
							try :
								data[items[z].attributes['uid'].value].append(L)
							except :
								data[items[z].attributes['uid'].value]=[L]
						elif o == 'CHRPOS ' :
							var=items[z].childNodes[y].firstChild.data
							try :
								data[items[z].attributes['uid'].value].append([var.split(":")[0],var.split(":")[1]])
							except :
								data[items[z].attributes['uid'].value]=[var.split(":")[0],var.split(":")[1]]
						elif o == 'SPDI' :
							try :
								data[items[z].attributes['uid'].value].append(items[z].childNodes[y].firstChild.data)
							except :
								data[items[z].attributes['uid'].value]=[items[z].childNodes[y].firstChild.data]
	for k in data.keys():
		fichier= "/opt/TFEwebsite/%s.fasta"%data[k][2][0]
		dchr= open(fichier,'r')
		tmp=int(data[k][2][1])
		if data[k][0] == "empty":
			dchr.seek(tmp-1)
			verif=dchr.read(1)
			data[k][0]=verif
		posi=tmp-101
		dchr.seek(posi)
		window=dchr.read(200)
		data[k].append(window)

	cmdtable="""CREATE TABLE IF NOT EXISTS %s (
	    id INT AUTO_INCREMENT PRIMARY KEY,
	    snpid varchar(25),
	    mut text,
	    gene text,
	    chr varchar(5),
	    pos text,
	    window text)
	    engine=MyISAM;""" % (keyword)	

	c.execute(cmdtable)	


	cmddata = """INSERT INTO """+str(keyword)+""" (snpid,mut,gene,chr,pos,window) VALUES (%s,%s,"%s",%s,%s,%s) """ #insertion database
	for key in data.keys():
		c.execute(cmddata,(key,data[key][1],data[key][0],data[key][2][0],data[key][2][1],data[key][3]))


   
"""#ki="test"
cmd = "CREATE TABLE IF NOT EXISTS %s (
         course  VARCHAR(15),
         student  VARCHAR(15),
         teacher VARCHAR(15),
         timeslot VARCHAR(15))
         ENGINE=MyISAM;" % (ki,)
#c.execute(cmd)"""
