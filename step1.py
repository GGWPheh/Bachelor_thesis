#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print
#  refreq.py
#  
#  Copyright 2020 root <root@Laptop Zehams & Kydae>
#  
import re
import pymysql
import time
import sys
keyword = sys.argv[1]

deb = time.time() #pour le temps

C=pymysql.connect(host="localhost",user="root",db="TFE",password="yy")
c=C.cursor()

df = open("/tmp/%s.txt"%keyword,"r")
# ~ df = open("./endo.txt","r")

text=df.read()
word=['gene','genes','Gene','Genes','protein','proteins','Protein','Proteins']
posPmid=[]
Dkeep={}
pattern = re.compile("PMID- ")
res = pattern.finditer(text)
for match in res:
	posPmid.append(match.start()) #donne la position
NombreDePMID = len(posPmid) #pour la verification
# ~ for i in range(len(posPmid)-1):
for i in range(NombreDePMID-1):
	# ~ print(i+1,"/",NombreDePMID-1) #verification
	for w in word:
		pattern = re.compile(r'[ */.:()"\n\'-]{}[ */.:;,?!()"\'-]'.format(w))
		match = pattern.search(text, posPmid[i], posPmid[i+1])
		if match:
			# ~ print(match)
			df.seek(posPmid[i])
			x = df.readline()
			x = x.strip().split("- ")[1]
			Dkeep[x]=[posPmid[i],posPmid[i+1]]
			
print("Nombre de PMID :",len(Dkeep),"/",NombreDePMID)			
IMP= ["DP  -","TI  -","AB  -","FAU -","PL  -","OAB -","OT  -"]
DATA={}
marker=False
var = 'important things missing'

for i in Dkeep.keys():
	Lbool=[False,False,False,False,False,False,False]
	s=[]
	df.seek(Dkeep[i][0])
	while df.tell() < Dkeep[i][1]:
		x=df.readline()
		if x.startswith("   ") == False:
			marker =False
			for pos,elem in enumerate(IMP):
				if x.startswith(elem):
					Lbool[pos]=True
					if var != x.strip().split("- ")[0]:
						if s:
							try:
								DATA[i].append(" ".join(s))
							except:
								DATA[i]=[" ".join(s)]
							s=[]
					
					var = x.strip().split("- ")[0]
					s.append(x.strip().split("- ")[1])
					marker=True
		if x.startswith(" ") and marker==True :
			s.append(x.strip())		
	try:	
		DATA[i].append(" ".join(s))
	except:
		
		DATA[i]=[" ".join(s)]
	s='empty'
	for pos,elem in enumerate(Lbool):
		if elem == False:
			DATA[i].insert(pos,s)
				
info = open("/tmp/onlyAB.usefull","w")
for key in Dkeep.keys():
	if DATA[key][2] !='empty':
		info.write(DATA[key][2])
		info.write("\n")
	if DATA[key][5] !='empty':
		info.write(DATA[key][5])
		info.write("\n")
info.close()
info = open("/tmp/pmidAB.usefull","w")
for key in Dkeep.keys():
	info.write("PMID- ")
	info.write(key)
	info.write("\n")
	if DATA[key][2] !='empty':
		info.write(DATA[key][2])
		info.write("\n")
	if DATA[key][5] !='empty':
		info.write(DATA[key][5])
		info.write("\n")
info.close()


cmdtable="""CREATE TABLE IF NOT EXISTS %s_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pmid int,
    date varchar(25),
    title text,
    ab text,
    oab text,
    author text,
    location text,
    keyword text)
    engine=MyISAM;""" % (keyword)	

c.execute(cmdtable)	

cmddata = """INSERT INTO """+str(keyword)+"""_data (pmid,date,title,ab,author,location,oab,keyword) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
for key in Dkeep.keys():
	c.execute(cmddata,(key,DATA[key][0],DATA[key][1],DATA[key][2],DATA[key][3],DATA[key][4],DATA[key][5],DATA[key][6]))

print("Insert Data succeed !!")
print(time.time()-deb,"sec")



"""
create table data(
    id INT AUTO_INCREMENT PRIMARY KEY,
    pmid int,
    date varchar(25),
    title text,
    ab text,
    oab text,
    author text,
    location text,
    keyword text)
    engine=MyISAM;
    
create table node(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    freq INT,
    nbnode INT,
    score INT,
    rel TEXT)
    ENGINE=MyISAM;
    
create table geneid(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    rel TEXT)
    ENGINE=MyISAM;
"""
