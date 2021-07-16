#Importation des modules nécessaire au fonctionnement du script
import requests
import tarfile
import subprocess
import os, sys
import yaml
import time

def readConf(monFichierYaml):
#Definition pour lire le fichier Yaml contenant les variables
	try:	
		with open (monFichierYaml, 'r') as stream:
			return yaml.safe_load(stream)
	except yaml.YAMLError as exc:
        	print(exc)

def myChown(path, uid, gid):
#Definition pour attribuer les droits nécessaires
	try:
		for root, dirs, files in os.walk(path):
			for dir in dirs:
				os.chown(os.path.join(root, dir), uid, gid)
			for file in files:
				os.chown(os.path.join(root, file), uid, gid)
	except: 
		print("erreur chown")

def telechargement (url, download):
#Definition pour télécharger l'archive' GLPI depuis un URL indiqué dans le fichier YAML
        try:
                response = requests.get(url, allow_redirects=True)
                with open(download,'wb') as file:
                        file.write(response.content)
        except:
                print ("erreur download de l'archive GLPI")
                
def untar (file, path):
#Definition pour décompresser l'archive GLPI vers le dossier tmp
        try:
                if file.endswith("tgz"):
                        tar = tarfile.open(file,"r:gz")
                        tar.extractall(path)
                        tar.close()
        except:
                print("erreur untar archive glpi")

def installpackage (package):
#Definition pour installer les paquets nécessaire à GLPI se trouvant dans le fichier YAML
	try:
		subprocess.call("apt install -y " + package, shell=True)
	except:
		print("erreur d'installation des paquets nécessaire")

def mysqlinstall (password):
#Définition pour créer la base de donnée mysql pour GLPI
	try:
		subprocess.run('mysql -e "CREATE DATABASE db_glpi"', shell=True)
		subprocess.run('mysql -e "GRANT ALL PRIVILEGES ON db_glpi.* TO admindb_glpi@localhost IDENTIFIED BY \'"'+ password + '"\'"', shell=True)
	
	except:	
		print("erreur création database")

def copie (extractdir, installdir):
#Definition pour supprimer la page apache2 par défaut et copier les fichier GLPI
	try:
		subprocess.run("rm "+ installdir + "/index.html", shell=True)
		subprocess.run("cp -r "+ extractdir +"/glpi/* "+ installdir, shell=True)
		
	except:
		print("erreur copie/droit") 

def installglpi (installdir, password):
#Definition pour installler GLPI en mode console 
	try:
		subprocess.run("php "+ installdir + "/bin/console db:install --reconfigure --default-language=en_GB --db-name=db_glpi --db-user=admindb_glpi --db-password= "+ password + " --force -n", shell=True)
	except:
		print("erreur installation glpi")

def reloadapache2 ():
#Définition pour redémarrer le service apache2
	try:
		subprocess.run("systemctl restart apache2", shell=True)
	except:
		print("erreur redemarrage apache")

def chown (dir):
#Definition pour attribuer les droits nécessaires à GLPI
	try:
		myChown(dir, 33, 33)
		time.sleep(10)
		myChown(dir, 33, 33)
	except:
		print("erreur droit fichier")

#Lancement des différents définitions

file = sys.argv[1]
vars = readConf(file)
telechargement(vars['URLGLPI'], vars['downloadFile'])
untar(vars['downloadFile'], vars['extractdir'])
for package in vars['packages']:
	installpackage(package)
mysqlinstall(vars['Passwordmysql'])
copie(vars['extractdir'], vars['repertory'])
installglpi(vars['repertory'], vars['Passwordmysql'])
reloadapache2()
chown(vars['repertory'])
