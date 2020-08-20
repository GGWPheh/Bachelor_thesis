#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pymysql



def mc(s):return """\n\t\t<td align=center>%s</td>"""%s
def mr(L):return """\n\n\t<tr >%s\n\t</tr>"""%"".join([mc(x) for x in L]) 
def mt(L):return """<table width= 1250px>%s\n\n</table>"""%"".join([mr(x) for x in L]) 

def makecheck(clas,name,value,desc,on,off):
	return """<input type=checkbox class="%s" name=%s value="%s" onchange="toggle(%s,%s)>%s : %s"""%(clas,name,value,on,off,value,desc)

def makerefresh():
	return """<button type="button" onclick="document.location.reload(true)">refresh</button>"""
def makedel(blid):
	return """<a href="del.cgi?blid=%s" onclick="return confirm('Etes vous sur de Supprimer ce fichier')"><input type="button" value="Supprimer"></a>"""%(blid)
def makeselect(blid):
	return """<a href="select.cgi?blid=%s"><input type="button" value="Visualiser"></a>"""%(blid)
def makerestart(blid):
	cmd="""select seq from job where id=%s"""
	c.execute(cmd,(blid))
	res, =c.fetchone()
	if res:return """<a href="restart.cgi?blid=%s"><input type="button" value="Restart"></a>"""%(blid)		
	else:return " OLD FILE"
def makekrona(blid):
	cmd="""select fmt from job where id=%s"""
	c.execute(cmd,(blid))
	res, =c.fetchone()
	if res:return """<a href="krona.cgi?blid=%s"><input type="button" value="Krona"></a>"""%(blid)		
	else:return " OLD FILE"
def makeinput(html,name,value,desc):
	return """<input type=%s name=%s value="%s">%s : %s<br>"""%(html,name,value,value,desc)
def findeformulaire():
	print """<input type="Submit" value="Envoyer"><input type="Reset" value="Reinitialiser les valeurs">
</form>"""





# ~ Programmes 
DP={} #        name , type-query , type-dbs, description
DP["blastn"]=('blastn','N','N',"Le programme blastn compare un acide nucleique avec les banques ADN")
DP["blastx"]=('blastx','N','P',"Le programme blastx compare un acide nucleique traduit en prot contre des banques de prot")
DP["blastp"]=('blastp','P','P',"Le programme blastp compare une proteine avec les banques de proteines")
DP["Tblastn"]=('Tblastn','P','N',"Le programme Tblastn compare une proteine a de l'ADN traduit en proteine")
DP["Tblastx"]=('Tblastx','N','N',"Le programme Tblastx compare de l'ADN a de l'ADN traduit en proteine")
# ~ DP["Psi-Blast"]=('Psi-Blast','P','P',"Le programme blastp compare une proteine avec les banques de proteines")
# ~ DP["Phi-Blast"]=('Phi-Blast','P','P',"Le programme blastp compare une proteine avec les banques de proteines")


# ~ Banques
DBB={} #		chemin, 		type ,			 des
DBB["swissprot"]=("/data/bblast/swissprot","P","la wonderful banque swissprot")
DBB["Gb Blast PLUS"]=("/data/bblast/gbblastpl","N","Une banque pour tous les fichiers Release de genbank")
DBB["gbblast"]=("/data/bblast/gbblast","N","Une banque pour tous les fichiers GENBANK")
DBB["16SMicrobial"]=("/data/genbank/BFPN/16SMicrobial","N","Une banque du gene 16S")
DBB["pataa"]=("/data/genbank/BFPN/pataa","P","Une banque pataafix, ca fix et ca refix")


