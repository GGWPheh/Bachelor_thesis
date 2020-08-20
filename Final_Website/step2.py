#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print
#  refreq.py
#  
#  Copyright 2020 root <root@Laptop Zehams & Kydae>
# 
import re
import sys
wts=sys.argv[1]   #where to read
sumfile=sys.argv[2] #where to write
import shelve
dg=open(wts)
gene=[]

for i in dg:
	gene.append(i.strip().split())


dc = open("/tmp/onlyAB.usefull","r")
onlyAB=dc.read()
""" TOUS LES ALIAS """
realgene=[]
for g in gene:
	use=[]
	for w in range(len(g)):
		pattern = re.compile(r'{}[ */.:;,?!()"\n\t\'-]'.format(g[w]))
		match=pattern.search(onlyAB)
		if match:
			use.append(g[w])
	if use:
		use.insert(0,g[0])
		realgene.append(use)
			
result=shelve.open(sumfile)
result["gene"]=realgene

print("Trier les genes finis !!")
