#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print()
print ("""<link rel= "stylesheet" type= "text/css" href="/TFE/Interface.css" />""")
print("<pre>")
print ("""<body>""")
print ("""<div class="miseenpage">""")
import sys 

keyword=sys.argv[1]

dwin=open("/tmp/%s.vcf"%keyword,"r")
text=dwin.readlines()
verif=0
for l in (text):
	if verif:print(l)
	if ("#CHROM") in l:
		print(l)
		verif = 1
	
print ("""</div>""")
print ("""</body>""")
print ("""	<footer>
		Mentions legales<br>
		&copy; Copyright <b>DOM - Database Of Mining</b> 2020	<br>
		Projet realise en fin de cycle de bachelier dans le but d'obtenir mon diplome en Bio-Informatiquen. Realise par <strong>Ahmed KANFOUD et Cyril RADERMECKER</strong>.
	</footer>""")
