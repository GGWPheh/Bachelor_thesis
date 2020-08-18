#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print()

print("<pre>")

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
	
