#!/usr/bin/env python2
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print
import cgi
import pymysql
import os
print "<pre>"

donnees=cgi.FieldStorage()
keyword = donnees.getvalue("keyword")

C=pymysql.connect(host="localhost",user="apache",db="SNP")
c=C.cursor()
cmd="select * from %s "
nb=c.execute(cmd,(keyword))

cmd="select res from job where id=%s"
c.execute(cmd,(blid))
res, = c.fetchone()
print res

