# TFEwebsite

MANUEL D'UTILISATION :

Nous avons mis toutes les images du fonctionnement du site dans le dossier /TFEwebsite/Final_Website/Screenshots

Si vous voulez utiliser le site, voici les étapes a réaliser :

-Installer le module python entrezpy

-Télécharger tout les fichiers de /TFEwebsite/Final_Website (exepté le dossier JS_CSS et Screenshots) et les placer dans un dossier /opt/dossier_site qui puisse être utilisé par apache. 

-Les fichiers js et css du dossier JS_CSS doivent se trouver dans le dossier /var/www/localhost/htdocs/TFE 

-Pour lancer la partie Alignement du site, il faut télécharger le génome humain chromosome par chromosome et enregister les fichiers de la manière suivante : "1.fasta =chromosome 1 / 2.fasta = chromosome 2 / ...". Tout ses fichiers devront se trouver dans le dossier /opt/dossier_site. 

-Et pour finir, il faut créer les databases SNP,GENE et EPI en donnant les privileges a apache.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TACHES NECESSAIRE :

-queue

IDEES D'AMELIORATION :

-Limiter les keyword sur une fourchette de lettre, ex : min 3 ltr => max 25 ltr
J'ai fais un test, mon prog bug quand le keyword contient "-" du coup faudrait empecher l'utilisateur de rentrer des caractères spéciaux
