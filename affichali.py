#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  refreq.py
#  
#  Copyright 2020 root <root@Laptop Zehams & Kydae>
# 
import pymysql
import sys 
import os

keyword=sys.argv[1]
keyfile = "/tmp/%s_res.vcf"%keyword
alreadydone=0

if not os.path.isfile(keyfile):
	dwin=open("/tmp/%s.vcf"%keyword,"r")
	text=dwin.read()
	dwin.close()
	df=open("/tmp/%s_res.vcf"%keyword,"w")
	df.write("Content-type:text/html")
	df.write("\n")
	df.write("<pre>")
	df.write("\n")
	df.write(text)
	df.close()
else :
	alreadydone +=1
