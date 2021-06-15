import requests
import tarfile
import subprocess

glpiUrl='https://github.com/glpi-project/glpi/releases/download/9.5.2/glpi-9.5.2.tgz'
downloadFile='/tmp/glpi-9.5.2.tgz'
extractDir = '/tmp'
Package = ["apache2", "php", "libapache2-mod-php", "mariadb-server", "php-mysqli", "php-mbstring", "php-curl", "php-gd", "php-simplexml", "php-intl", "php-ldap", "php-apcu", "php-xmlrpc", "php-cas", "php-zip", "php-bz2", "php-ldap",	"php-imap"]                     
        
def telechargement (url, download):
#import requests
        try:
                response = requests.get(url, allow_redirects=True)
                with open(download,'wb') as file:
                        file.write(response.content)
        except:
                print ("erreur1")
                
def untar (file, path):
#import tarfile
        try:
                if file.endswith("tgz"):
                        tar = tarfile.open(file,"r:gz")
                        tar.extractall(path)
                        tar.close()
        except:
                print("erreur2")

def installpackage (onepackagetoinstall): 
#apt install package
        try:
                 subprocess.call("apt install -y " + onepackagetoinstall, shell=True)
        except:
                print("erreur3")

def package2 ():
#apt install package+
        try:
                subprocess.call("apt install php-mysqli php-mbstring php-curl php-gd php-simplexml php-intl php-ldap php-apcu php-xmlrpc php-cas php-zip php-bz2 php-ldap 			php-imap -y", shell=True)
        except:
                print("erreur4")

#def mysqlinstall ():
#	try:
#		subprocess.call("mysql_secure_installation", shell=True)
#		subprocess.call("y", shell=True)
#	except:
#		print("erreur5")

#def mysqlinstall2 ():
#	try:
#		subprocess.call("mysql -u root -p", shell=True)
#		subprocess.call("create database db_glpi;", shell=True)

#menu()
telechargement(glpiUrl, downloadFile)
untar(downloadFile, extractDir)
for onePackage in Package:
  installpackage(onePackage)
package2()
#mysqlinstall()
