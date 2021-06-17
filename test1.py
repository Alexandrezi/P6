import requests
import tarfile
import subprocess
import os

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

#def mysqlinstall ():
#	try:
		os.system("mysql_secure_installation", shell=True)
#		subprocess.call("y", shell=True)
#	except:
#		print("erreur5")

#def mysqlinstall2 ():
#	try:
		os.system("mysql -u root -p=Alex0603!")
#		subprocess.call("create database db_glpi;", shell=True)


def copie ():
	try:
		os.system("shopt -s dotglob")
		os.system("rm /var/www/html/index.html")
		os.system("cp -r /tmp/glpi/* /var/www/html")
		os.system("chown -R www-data /var/www/html")
	except:
		print("erreur copie/droit") 

def installglpi ():
	try:
		os.system("php /var/www/html/bin/console db:install --reconfigure --default-language=en_GB --db-name=db_glpi --db-user=admindb_glpi --db-password=MDP --force -n")
	except:
		print("erreur installation glpi")


telechargement(glpiUrl, downloadFile)
untar(downloadFile, extractDir)
for onePackage in Package:
  installpackage(onePackage)
#mysqlinstall()
copie()
installglpi()
