import requests
import tarfile
import subprocess
import os, sys
import yaml
import time

def readConf(monFichierYaml):
	try:	
		with open (monFichierYaml, 'r') as stream:
			return yaml.safe_load(stream)
	except yaml.YAMLError as exc:
        	print(exc)

def myChown(path, uid, gid):
	try:
		for root, dirs, files in os.walk(path):
			for dir in dirs:
				os.chown(os.path.join(root, dir), uid, gid)
			for file in files:
				os.chown(os.path.join(root, file), uid, gid)
	except: 
		print("erreur")

def telechargement (url, download):
#import requests
        try:
                response = requests.get(url, allow_redirects=True)
                with open(download,'wb') as file:
                        file.write(response.content)
        except:
                print ("erreur download")
                
def untar (file, path):
#import tarfile
        try:
                if file.endswith("tgz"):
                        tar = tarfile.open(file,"r:gz")
                        tar.extractall(path)
                        tar.close()
        except:
                print("erreur tar")

def installpackage (package):
#apt install package
	try:
		subprocess.call("apt install -y " + package, shell=True)
	except:
		print("x")

def mysqlinstall ():
#installation base de données
	try:
		subprocess.run('mysql -e "CREATE DATABASE db_glpi"', shell=True)
		subprocess.run('mysql -e "GRANT ALL PRIVILEGES ON db_glpi.* TO admindb_glpi@localhost IDENTIFIED BY \'MDP\'"', shell=True)
	
	except:	
		print("erreur création database")

def copie (extractdir, installdir):
	try:
		subprocess.run("rm "+ installdir + "/index.html", shell=True)
		subprocess.run("cp -r "+ extractdir +"/glpi/* "+ installdir, shell=True)
		
	except:
		print("erreur copie/droit") 

def installglpi (installdir):
	try:
		subprocess.run("php "+ installdir + "/bin/console db:install --reconfigure --default-language=en_GB --db-name=db_glpi --db-user=admindb_glpi --db-password=MDP --force -n", shell=True)
	except:
		print("erreur installation glpi")

def reloadapache2 ():
	try:
		subprocess.run("systemctl restart apache2", shell=True)
	except:
		print("erreur redemarrage apache")
def chown (dir):
	try:
		myChown(dir, 33, 33)
		time.sleep(10)
		myChown(dir, 33, 33)
	except:
		print("erreur droit fichier")

file = sys.argv[1]
vars = readConf(file)
telechargement(vars['URLGLPI'], vars['downloadFile'])
untar(vars['downloadFile'], vars['extractdir'])
for package in vars['packages']:
	installpackage(package)
mysqlinstall()
copie(vars['extractdir'], vars['repertory'])
installglpi(vars['repertory'])
reloadapache2()
chown(vars['repertory'])
