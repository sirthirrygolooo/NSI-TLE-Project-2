# Compte Rendu Final

*Groupe BROUILLET Arthur, POIRIER Louis, FROEHLY Jean-BAptiste

## Introduction 

Pour rappel, notre projet était de créer un système de vote en ligne basé sur une blockchain. Pour cela nous avons utilisé python et la POO pour la blockchain, et le framework flask pour la parti web-frontend controlable depuis python.

## Le projet 

Structure :

```
Aroborescence du projet


├── README.md
├── project
│   ├── __init__.py
│   ├── admin
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   ├── style_about.css
│   │   │   ├── style_login.css
│   │   │   ├── style_para.css
│   │   │   ├── style_vote.css
│   │   │   ├── style_voted.css
│   │   │   ├── style.css	
│   │   ├── img
│   │   ├── js
│   │   │   ├── script_login.js
│   │   │   ├── script_para.js
│   │   |   ├── script.js
│   ├── templates
│   │   ├── about.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── presentation.html
│   │   ├── vote.html
│   │   ├── voted.html
│   ├── __init__.py
│   ├── config.py
|
├── requirements.txt
├── blockch.py
├── datas.py
├── run.py

```

### Fonctionnement

Le fonctionnement du projet est donc le suivant :  
Le fichier [`run.py`](./../run.py 'go to file') vérifique que les libs requises sont installées et lance le serveur flask. Ensuite, si le lien est sous la forme `127.0.0.1:5000/`(car hébergé en local), alors tout va se passer dans le fichier [`/main/routes.py`](./../project/main/routes.py 'go to file') qui va définir toutes ce qu'il faut selon le chemin tandis que si le lien est sous la forme `127.0.0.1:5000/admin/` alors tout va se passer dans le fichier `/admin/routes.py` qui va définir les routes côté admin. Tout ceci est défini dans le fichier [`__init__.py`](../project/__init__.py 'go to file') qui vient fixer les différentes routes possibles et la config utilisée. Ensuite, on indique pour chaque route les pages html à charger (dans le dossier `/templates`) et n'ayant pas tant de fonctions utiliser, elles sont pour la plupart aussi stockées dedans. On retrouve aussi un fichier [`datas.py`](./../datas.py 'go to file') qui contient toute les données relatives aux candidats (car nous n'avont pas fait de registres côté admin pour les gérer) et aux calculs de stats quand calculs il y a. Enfin, depuis le panel admin, on peut accéder à l'ensemble de la blockchain et vérifier sa validité (en vérifiant les hash et les signatures), les blocs s'ajoutant automatiquement à chaque vote.



## Notre travail

### Arthur



### Louis



### J-B