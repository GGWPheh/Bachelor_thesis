#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\n")
print()

import os
import cgi


donnees=cgi.FieldStorage()
gene = donnees.getvalue("gene_query")
keyword = donnees.getvalue("keyword")

cmd ="""python Extraction.py %s %s"""%(gene,keyword)
os.system(cmd)

