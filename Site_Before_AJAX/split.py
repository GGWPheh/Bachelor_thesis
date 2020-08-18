#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print
#  split.py
#  
#  Copyright 2020 root <root@Laptop Zehams>

import time

deb = time.time() #pour le temps

df = open("/opt/TFEwebsite/clear_human_genome")
text = df.readlines()
part=1
namefile="/tmp/gene.%s.part"%part

l=0
wf=open(namefile,"w")
for i in text:
	if l < 500:
		wf.write(i)
	else:	
		l=0
		part+=1
		wf.close()	
		namefile="/tmp/gene.%s.part"%part
		wf=open(namefile,"w")
	l+=1

print("SPLIT succeed !!")
print(time.time()-deb,"sec")
