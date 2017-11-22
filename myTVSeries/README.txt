Bonjour Monsieur Poli et soyez le bienvenu sur ce projet !
Nous avons utilisé Docker durant le développement de ce projet, mais voici nos recommandations afin de lancer notre projet :

1 - Installer python 3.4

2 - Installer Django 1.11

    RUN pip install Django==1.11

3 - Installer requests

    RUN pip install requests

4 - Installer psycopg2

    RUN pip install psycopg2

5 - Se placer dans le dossier et lancer le projet avec :

    python manage.py runserver

6 - lancer http://localhost:8000 dans un navigateur

7 - Bon courage :)



Au cas où, notre projet se trouve ici : https://github.com/Irisa7/TV-Series








/////// Consignes internes pour le développement du projet ////////

Prérequis : avoir installé Docker

1 - Se placer dans son dossier de travail (racine)
2 - git pull pour mettre à jour les changements des copains :)
3 - taper "docker-compose up" dans le terminal pour activer le docker.

/// ACHARNEMENT, GOUTTES DE SUEUR, ETC. ///

Avant de partir :

0 - Ctrl + C (on quitte le runserver)
1 - On supprime touuuuuuus ses pycaches !!
2 - git status (on vérifie nos changements)
3 - git add ... (on ajoute les nouveaux fichiers)
4 - git commit -m "Description du commit"
5 - git push (on push sur sa branche)
6 - sur gitHub, on Pull Requests, puis on Merge
7 - on va boire une bière pour fêter la fin de cette bonne session de travail :)
