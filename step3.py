#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print
#  refreq.py
#  
#  Copyright 2020 root <root@Laptop Zehams & Kydae>
#  
import time

deb = time.time() #pour le temps

import re
import pymysql
C=pymysql.connect(host="localhost",user="root",db="TFE",password="yy")
c=C.cursor()

dg=open("/tmp/gene.usefull","r")
DGkeep={}
for l in dg:
	a=l.split()
	DGkeep[a[0]]=a[1:]
	
da=open("/tmp/pmidAB.usefull","r")
pmidAB=da.read()
posPmid=[]
Dkeep={}

print("Search for PMID-")

pattern = re.compile("PMID- ")
res = pattern.finditer(pmidAB)
for match in res:
	posPmid.append(match.start())
	
NombreDePMID = len(posPmid) #pour la verification
for i in range(len(posPmid)):
	print("PMID",i+1,"/",NombreDePMID) #verification	
	da.seek(posPmid[i])
	x = da.readline()
	x = x.strip().split("- ")[1]
	try:
		Dkeep[x]=[posPmid[i],posPmid[i+1]]
	except:
		da.readline()
		end = da.tell()
		Dkeep[x]=[posPmid[i],end]

print("Search for frequence")
	
DFG={}
DNG={}
Lnode=[]

NombreDeGene = len(DGkeep.keys())
v = 0
for g in DGkeep.keys():
	print("GENE",v,"/",NombreDeGene) #verification
	v+=1
	refreq=0
	for w in range(len(DGkeep[g])):
		for key in Dkeep.keys():
			pattern = re.compile(r'[ */.:;,?!()"\n\']{}[ */.:;,?!()"\'-]'.format(DGkeep[g][w]))
			nbmatch=pattern.findall(pmidAB, Dkeep[key][0], Dkeep[key][1])
			refreq += len(nbmatch)
			if nbmatch:
				Lnode.append(key)
	if refreq != 0:
		DFG[g]=refreq
		DNG[g]=Lnode
		Lnode=[]
		


print("Search for nodes")		
		
nameGene = [k for k in DNG.keys()]
NODE={}
LienNG={}
noeud = 0
nomdegene=set() 
inutile = 0

NombreDeNode = len(nameGene)

for i in range(len(nameGene)):
	print("NODE",i,"/",NombreDeNode) #verification
	NODE[nameGene[i]]=[noeud]
	for j in range(len(DNG[nameGene[i]])):
		for k in range(len(nameGene)):
			if nameGene[i] == nameGene[k]:
					inutile = 0
			elif (DNG[nameGene[i]][j] in DNG[nameGene[k]]):
				nomdegene.add(nameGene[k])
				noeud += 1
		NODE[nameGene[i]].append(noeud)
		noeud=0
	LienNG[nameGene[i]]=list(nomdegene)
	nomdegene=set()
	
for i in NODE:
	NODE[i]=sum(NODE[i])

cmdtable="""CREATE TABLE IF NOT EXISTS %s_node(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    freq INT,
    nbnode INT,
    score INT,
    rel TEXT,
    pmid TEXT)
    ENGINE=MyISAM;""" % (keyword)	

c.execute(cmdtable)	

cmdnode = """INSERT INTO """+str(keyword)+"""_node (name,freq,nbnode,score,rel,pmid) VALUES (%s,"%s","%s",%s,"%s","%s") """
for key in DFG.keys():
	score = DFG[key]*NODE[key]
	c.execute(cmdnode,(key,DFG[key],NODE[key],score,LienNG[key],DNG[key]))
	
#cmdgeneid = """INSERT INTO geneid (name,rel) VALUES (%s,"%s") """
#for key in DNG.keys():
#	c.execute(cmdgeneid,(key,DNG[key]))
print("Insert NODE succeed !!")
print(time.time()-deb,"sec")
