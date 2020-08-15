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

C=pymysql.connect(host="localhost",user="root",db="SNP",password="yy")
c=C.cursor()

keyword=sys.argv[1]
keyfile = "/tmp/%s_window.txt"%keyword
cmd="""select snpid,window from %s""" % (keyword)
alreadydone=0

if not os.path.isfile(keyfile):
	c.execute(cmd)
	var=c.fetchall()
	# ~ print (var)
	dwin=open("/tmp/%s_window.txt"%keyword,"w")
	for i in var :
		vor=list(i)
		dwin.write(">")
		dwin.write(vor[0])
		dwin.write("\n")
		dwin.write(vor[1])
		dwin.write("\n")
	dwin.close()
else :
	alreadydone +=1

