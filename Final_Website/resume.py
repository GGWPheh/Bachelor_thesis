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

import shelve
df=open("/tmp/gene.usefull","w")
for i in range(1,125):
	result=shelve.open("/tmp/gene.%s.summary"%i)
	gene=result["gene"]
	for l in gene:
		for k in range(len(l)):
			df.write(l[k])
			df.write(" ")
		df.write("\n")
df.close()

print("RESUME succeed !!")
print(time.time()-deb,"sec")
