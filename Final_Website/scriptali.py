#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2020 root <root@Laptop Zehams & Kydae>
# 
import pymysql
import sys 
import os

C=pymysql.connect(host="localhost",user="root",db="SNP",password="yy")
c=C.cursor()

keyword=sys.argv[1]
keyfile = "/tmp/%s_window.txt"%keyword


cmd="""select snpid,window from %s"""%(keyword)
c.execute(cmd)
var=c.fetchall()

dwin=open("/tmp/%s_window.txt"%keyword,"w")
for i in var :
	vor=list(i)
	dwin.write(">")
	dwin.write(vor[0])
	dwin.write("\n")
	dwin.write(vor[1])
	dwin.write("\n")
dwin.close()

