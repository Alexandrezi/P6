## Information générale

Ce script permet le téléchargement et l'installation automatiques des paquets requis et d'installer GLPI.

## Prérequis 

* python3 - "apt install python3" si non installé
* pip3 - "apt install python3-pip"
* yaml - "pip3 install pyyaml"

## Utilisation

Pour démarrer le script, utiliser cette commande dans le terminal :
`python3 script.py packages.yaml`

Pour changer les fichier de destinations :

Aller dans le fichier yaml, vous pouvez modifier chacun de ces éléments :  
* "URLGLPI" :URL de l'archive GLPI
* "downloadFire" :répertoire où le paquet GLPI sera stocké
* "extractdir" :répertoire de destination temporaire de la décompression de l'archive GLPI
* "repertory" :répertoire de final des fichier GLPI
* "Passwordglpi" :mot de passe de la base de donnée GLPI

## Code erreur

* 1 = Erreur de lecture du fichier Yaml
* 2 = Erreur droit fichier
* 3 = Erreur téléchargement archive GLPI
* 4 = Erreur décompression archive GLPI
* 5 = Erreur installation des paquets nécessaires
* 6 = Erreur création database mysql
* 7 = Erreur copie des fichiers glpi / supression index.html
* 8 = Erreur installation glpi
* 9 = Erreur redémarrage Apache2
* 10 = Erreur droit fichier



