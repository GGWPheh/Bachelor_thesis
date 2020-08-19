#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")

#  Copyright 2020 root <root@GGWP>
#  
import pymysql
import sys 

keyword=sys.argv[1]
C=pymysql.connect(host="localhost",user="root",db="SNP",password="yy")
c=C.cursor()
cmd="""select gene from %s;"""% (keyword)
c.execute(cmd)
res=c.fetchall()

gene_snp_not_Set=[]
for i in res :
	first_clear=i[0].split("'")
	for y in range (len(first_clear)) :
		if y % 2 != 0 :
			gene_snp_not_Set.append(first_clear[y])
			
gene_snp = list(set(gene_snp_not_Set))

# ~ print(gene_snp)

C=pymysql.connect(host="localhost",user="root",db="GENE",password="yy")
c=C.cursor()
cmd="""select name from %s_node;"""% (keyword)
c.execute(cmd)
res=c.fetchall()

gene_gene=[]
for i in res :
	gene_gene.append(i[0])

pourcentage=0
for y in gene_gene :
	for x in gene_snp :
		if y == x :
			pourcentage +=1
if len(gene_snp) < len(gene_gene) :
	Final_res=pourcentage/len(gene_gene)
	
else :
	Final_res=pourcentage/len(gene_snp)
	
print ("La liste des genes avec SNP research : ","						","La liste des genes avec Gene research : ")
for a in gene_snp :
	for b in gene_gene :
		print (a,"						",b)
print ("Pourcentage de similarités entre les deux listes : ",Final_res*100)
# ~ print(gene_gene)
# ~ print("----------")
# ~ print(gene_snp)
