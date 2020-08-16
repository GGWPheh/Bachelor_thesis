# TFEwebsite

NOTES POUR LE RAPPORT :

RAJOUTER LES NOTES DE SLITE !!!!

Afin que l'utilisateur puisse utiliser nos programmes sur n'importe quel mot clé, ils nous a fallut trouver un moyen de télécharger les fichiers nécessaire sur le ncbi de manière automatique. Ils nous as fallut pas mal de temps avant de trouver une piste concrete (rajouter des mauvaises pistes ?). Après nous avons découvert E-utilites, qui est un système de neuf serveurs (mis en place par le ncbi) répondant a des rêquetes url afin de fournir l'élément désiré. Cependant il n'était pas aisé d'intégrer cela dans nos scripts python, la synthax de ces requêtes url n'etant pas simple et il est aussi difficile de traiter la réponse fournie par le serveur. Nous avons donc commencer a rechercher après des manières plus aisé de combiner E-utilites et python. Nous avons fini par trouver Entrezpy, qui est un module python permmettant de traiter avec E-utilites de manière simplifier. Ils nous a fallut apprendre comment utiliser ce nouveau module, pour cela nous avons utilisé leur site officiel. La tache ne fut spécialement aisée car leur tutoriel contenait des erreurs. Après de multiples tests en python interactif pour être bien sur que l'on savait utiliser ce nouveau module nous l'avons intégré dans nos scripts. Malheureusement, un des fichiers nécessaire a mon programme n'était pas disponible en .txt (expliquer les vérifications pour trouver l'erreur : l'erreur vient du ncbi). Premièrement j'ai voulu trouvé un moyen de convertir un .xml en .txt mais impossible a part avec des service web, ce qui aurait empeché l'automatisation. J'ai donc du réécrire mon script pour qu'il fonctionne avec des fichiers xml. Traiter du xml avec les connaissances que j'avais était très compliqué. J'ai donc commencer a rechercher après un moyen de traiter des fichiers xml avec python. Je suis tombé sur la librairie Element tree, j'ai commencé a apprendre cette nouvelle synthax. Je me suis ensuite entrainé a l'utiliser en python interactif avant de me lancer dans l'élaboration de mon script 2.0
J'ai réussi a adapter mon script pour obtenir les memes résultats qu'avant. Seulement je n'ai pas pu insérer le nucléotide de base et le muté de manière séparer. Heureusement j'ai quand même pu obtenir cette info mais elle est juste sous une moins belle forme. A partir de la, nos programmes tournaient sur le site mais il restait encore quelques détails a régler. Il nous fallait rendre la création des tables dynamique et aussi faire en sorte que le programme ne retélécharge pas des informations déjà présente dans la database. 

DEBRIEF :

-Le datamining fonctionne pour nous deux. J'ai mis en commentaire un INSERT dans step3, je comprenais pas a quoi servait cette table.

-J'arrive pas a régler le problème pour afficher les resultats de l'alignement. Mais sinon l'alignement fonctionne j'ai vérifié.

-En faisant des tests j'ai remarqué qu'il faut qu'on trouve une condition pour qu'il ne rajoute pas dans la database si elle existe déjà (fichier concerné : step1, step3, scriptml) EDIT : j'ai réglé le problème chez moi, je pense que la solution peut s'appliquer aussi a ton script
REEDIT: j'ai appliqué la même condition dans tes fichiers et ca fonctionne (il fait quand meme un truc inutile mais c'est deja mieux) et j'ai profité de cette condition pour mettre le telechargement conduit avec. Du coup j'ai plus de step0... (mais c'est plus efficace). J'ai pas changé ces dernieres etapes ici parce que je prefere que tu valides avant (enfin je l'ai fais dans mes fichiers).


TACHES NECESSAIRE :

-boutons pour visualiser database (bouton keyword => SELECT FROM keyword)

-retour sur la page d'accueil

-queue

-CSS/JAVA/truc joli quoi...

IDEES D'AMELIORATION :

vas y lache toi sur les idées de fou :D

-Mettre le lien d'un css dans les balises html ?

-Limiter les keyword sur une fourchette de lettre, ex : min 3 ltr => max 25 ltr
J'ai fais un test, mon prog bug quand le keyword contient "-" du coup faudrait empecher l'utilisateur de rentrer des caractères spéciaux
