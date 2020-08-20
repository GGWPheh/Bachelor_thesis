#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print ()
print ("""<link rel= "stylesheet" type= "text/css" href="/TFE/Interface.css" />""")
print ("<pre>")

print ("""<body>""")
print ("""<div class="miseenpage">""")


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

common_gene=[]
other_gene=[]
pourcentage=0
for y in gene_gene :
	for x in gene_snp :
		if y == x :
			pourcentage +=1
			common_gene.append(y)
		else :
			other_gene.append(x)
			other_gene.append(y)
if len(gene_snp) < len(gene_gene) :
	Final_res=pourcentage/len(gene_gene)
	
else :
	Final_res=pourcentage/len(gene_snp)

other_gene = list(set(other_gene))
print ("<br>Pourcentage de similarites entre les deux listes : ",Final_res*100,"%")
print("<br>----------")	
print ("<br>La liste des genes en commun : <br>")
taille_common=len(common_gene)//8 +1
taille_other=len(other_gene)//8 +1
for a in range(len(common_gene)) :
	for x in range(1,taille_common) :
		if a == x*8 :
			print ("<br>")
	print (common_gene[a],", ")
print("<br>----------")	
print ("<br>La liste des genes differents : <br>")
for b in range(len(other_gene)) :
	for y in range(1,taille_other) :
		if b == y*8 :
			print ("<br>")
	print (other_gene[b],",",end='')
print("<br>----------")	


	
print ("""</div>""")
print ("""</body>""")
print("""	<footer>
		Mentions legales<br>
		&copy; Copyright <b>DOM - Database Of Mining</b> 2020	<br>
		Projet realise en fin de cycle de bachelier dans le but d'obtenir mon diplome en Bio-Informatiquen. Realise par <strong>Ahmed KANFOUD et Cyril RADERMECKER</strong>.
	</footer>""")
