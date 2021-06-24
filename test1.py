import requests
import tarfile
import subprocess


glpiUrl='https://github.com/glpi-project/glpi/releases/download/9.5.2/glpi-9.5.2.tgz'
downloadFile='/tmp/glpi-9.5.2.tgz'
extractDir = '/tmp'
Package = ["apache2", "php", "libapache2-mod-php", "mariadb-server", "php-mysqli", "php-mbstring", "php-curl", "php-gd", "php-simplexml", "php-intl", "php-ldap", "php-apcu", "php-xmlrpc", "php-cas", "php-zip", "php-bz2", "php-ldap", "php-imap"]
        
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

def installpackage (onepackagetoinstall): 
#apt install package
        try:
                 subprocess.call("apt install -y " + onepackagetoinstall, shell=True)
        except:
                print("erreur install package")

def mysqlinstall ():
#installation base de données
	try:
		subprocess.run('mysql -e "CREATE DATABASE db_glpi"', shell=True)
		subprocess.run('mysql -e "GRANT ALL PRIVILEGES ON db_glpi.* TO 		 	admindb_glpi@localhost"', shell=True)
	
	except:

def copie ():
	try:
		subprocess.run("rm /var/www/html/index.html", shell=True)
		subprocess.run("cp -r /tmp/glpi/* /var/www/html", shell=True)
		subprocess.run("chown -R www-data /var/www/html", shell=True)
	except:
		print("erreur copie/droit") 

def installglpi ():
	try:
		subprocess.run("php /var/www/html/bin/console db:install --reconfigure --default-language=en_GB --db-name=db_glpi --db-user=admindb_glpi --db-password=MDP --force -n", shell=True)
	except:
		print("erreur installation glpi")


telechargement(glpiUrl, downloadFile)
untar(downloadFile, extractDir)
for onePackage in Package:
  installpackage(onePackage)
mysqlinstall()
copie()
installglpi()
