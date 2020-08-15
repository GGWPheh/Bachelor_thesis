#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  refreq.py
#  
#  Copyright 2020 root <root@Laptop Zehams & Kydae>
# 
import pymysql
import sys 

C=pymysql.connect(host="localhost",user="root",db="test",password="yy")
c=C.cursor()

keyword=sys.argv[1]

cmd="""select snpid,window from data limit 3"""
c.execute(cmd)
var=c.fetchall()
# ~ print (var)
dwin=open("./%s_window.txt","w")%keyword
for i in var :
	vor=list(i)
	dwin.write(">")
	dwin.write(vor[0])
	dwin.write("\n")
	dwin.write(vor[1])
	dwin.write("\n")
dwin.close()

