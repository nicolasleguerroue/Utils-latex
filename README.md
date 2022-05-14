# Sources Latex

Ce document résume l'utilisation des sources Latex pour une utilisation personnelle sous Linux.

Le langage Latex n'est pas le plus simple à prendre un main mais permet de rédiger des documents de qualité.

Un tutoriel détaillé sur l'utilisation des sources est disponible dans le document ```Documentation_Latex.pdf```

## Présentation

Ce document a pour but de présenter les fonctionnalités de la bibliothèque Utils, qui n'est qu'un regroupement de bibliothèques pour simplifier l'utilisation de Latex.

Chaque bibliothèque doit être indépendante afin de fonctionner correctement.

Voici les bibliothèques disponibles: 


- Badges
- Colors
- Debug
- Electronic
- Fonts
- Glossaries
- Graphics
- Header
- Images
- Index
- Items
- Labels
- Layout
- Links
- Maths
- MessageBox
- Nomenclature
- Objects3D
- Pdf
- Programming
- Theorems
- Titles
- Tree


## Installation

Latex est un logiciel assez volumineux - Environ 1.5Go dans les dépots Debian/Ubuntu - mais l'installation complète ne nécéssite pas d'ajout de paquet supplémentaires.

Il est disponible dans les dépots ```Debian/Ubuntu``` avec les commandes suivantes :

```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install texlive-full
```

La commande suivante permet de gérer Latex en français.

```
sudo apt-get install texlive-lang-european
```

***L'ensemble des outils présenté est optimisé pour une utilsation avec le logiciel Visual Studio Code***

### Installation de Visual Studio Code
```
sudo snap install code
```

Enfin, l'installation de PHP permettra de générer le code d'autocomplétion pour VSCode

### Installation du module PHP
```
sudo apt-get install php
```

## Organisation du projet

Le projet est consitué de 6 dossiers et de 3 fichiers situés à la racine du projet.


- Le dossier ```Images``` contient l'ensemble des images du projet.

    Chaque image doit faire partie de la même partie que son document source associé.

- Le dossier ```Make``` contient les fichiers annexes du projet: 

    - Le fichier ```Bibliography.tex``` recense les bibliographies du projet. Le format Zotéro est compatible.
    - Le fichier ```Contacts.tex``` est une page pour contacter l'auteur et contient les informations sur les droits et les licences du projet.
    - Le fichier ```Versions.tex``` contient les différentes versions du projet.
    - Le fichier ```Glossaries.tex``` contient le glosssaire.
    - Le fichier ```Index.tex``` contient l'index.
    - Le fichier ```Nomenclature.tex``` contient la nomenclature\footnote{Les unités et grandeurs physiques par exemple
    - Le fichier ```Rules.tex``` contient les conventions pour le projet. Il peut contenir les types de commandes, les conventions de nommage du projet..

- Le dossier ```Output``` contient les fichiers de compilation générés de manière automatique. Vous n'aurez pas à modifier des fichiers à cette emplacement.

- Le dossier ```Parts``` contient les différentes parties du projet. Il est possible de scinder son projet en grandes parties (Introduction, Chapitre1, Chapitre2, Conclusion), chaque dossier contenu dans le dossier ```Parts``` représente ces parties.\\

Dans chacun de ces dossier, vous pouvez créer autant de fichier Latex que vous voulez, il seront compilés dans l'ordre alphabétique ou bien par ordre croissant si vous mettre un numéro au début du nom de fichier.\\

Pour chaque dossier crée dans le dossier ```Parts```, il faudra créer un dossier avec le même nom dans le dossier ```Images```, sous peine de voir une volée d'erreur lors de la compilation (Voir l'arborescence du projet).
    
- Le dossier ```Utils``` contient les bibliothèques du projet.
- Le dossier ```.vscode``` (dossier caché) contient les fichiers des paramètres VSCode.

Et voici les trois fichiers situés à la racine: 

- Le fichier ```Settings.tex``` regroupe les paramètres de mise en page du projet
- Le fichier ```main.tex``` est le fichier principal du projet.
- Le fichier ```make``` est le fichier de compilation.


## Fusion de projets

Le choix d'un dossier par partie (Parts/XXX) permet de fusionner très facilement des projets.
Pour fusionner deux projets, il suffit de copier-coller le contenu du dossier ```Images``` et ```Parts``` du projet A dans le dossier de projet qui contiendra la fusion (projet B). Lors de la compilation, ```make``` va gérer la fusion automatiquement.


## Compilation du projet

### Première compilation

La compilation du projet se fait grâce au fichier ```make``` situé à la racine du projet.
Avant de faire la toute première compilation, il convient de rendre éxécutable le fichier ```make``` en saissisant la commande suivante : 
    
#### Don des droits d'éxécution sur le fichier ```make```
```
chmod +x make
```

Il ne reste plus qu'à compiler le fichier.

### Compilation classique

Une compilation classique a pour objectif de générer le fichier PDF de rendu, appelé ```main.pdf``` et situé à la racine du projet.
### Compilation du projet
```
./make
```

Lors de la compilation, plusieurs fichiers sont générés à la racine, dont : 


- Le fichier ```.render_report.tex``` (fichier caché) qui contient la première partie des fichiers journaux de compilation
- Le fichier ```.render_report\_logs.tex``` qui contient la seconde partie des fichiers journaux de compilation
- Le fichier **standlone.tex** est le fichier qui contient l'intégralité du projet (bibliothèques et code sources du projet). Ce dernier est donc utilisable avec la commande **pdflatex** et permet de générer le fichier PDF à lui seul.

  
- Une image ```Part.png``` qui affiche le nombre de ligne pour chaque fichier contenu dans le dossier ```Parts```

- Une image ```Utils.png``` qui affiche le nombre de ligne pour chaque fichier contenu dans le dossier ```Utils```



### Vérification orthographique

En invoquant le paramètre ```--check```, il est possible de faire une vérification orthographique avec le logiciel aspell. Ci ce dernier n'est pas installé, il suffit de lancer la commande suivante : 

#### Installation de aspell
```
sudo apt-get install -y aspell
```

Enfin, si vous lancer la commande 

```
./make --check
```

Le fichier ```make``` vous demande si vous souhaiter corriger les fichiers contenus dans le dossier ```Parts```.


Veuillez saisir **y** si vous souhaitez corriger le fichier indiqué.

Ensuite, il ne vous reste plus qu'à être guidé par le logiciel aspell.


Les commandes sont à saisir au clavier (**Ctrl+I** pour ignorer le mot par exemple).

### Mise à jour Git

Pour les projets Latex étant sur Git, il est possible de mettre à jour le dépot en saississant la commande suivante : 
```
./make --git
```




### Mise à jour de l'autocomplétion

Il est possible de mettre à jour l'autocomplétion sous VScode pour les bibliothèques Utils.
En invoquant le paramètre ```--snippet```, il est possible de générer le fichier VScode qui va ajouter l'autocomplétion.

Ce fichier est appelée ```output.snippet-code``` et se situe dans le dossier ```.vscode```

```
./make --snippet
```


### Compilation avec VSCode

Toutes les commandes invoquées avec $make$ sont accessibles en ouvrant le répertoire du projet avec VScode;
Il suffit de se placer à la racine du projet et de faire la commande suivante:

```
code .
```


L'ensemble des commandes et outils sont disponibles en saissisant le raccourci **CTRT+SHIFT+B** 

