import requests
import tarfile
import subprocess

glpiUrl='https://github.com/glpi-project/glpi/releases/download/9.5.2/glpi-9.5.2.tgz'
downloadFile='/tmp/glpi-9.5.2.tgz'
extractDir = '/tmp'

def menu ():
        choix = int(input("faire son choix"))
        if choix == "1":
                telechargement()
                untar ()
                print ("téléchargemrnt + untar")
        else:
                print ("probleme")
                        
        
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

def package ():
        try:
#                package_name = "<apache2><php><libapache2-mod-php><mariadb-server>"
#                subprocess.run(["apt", "install", "-y", package_name], check=True)
                 subprocess.call("apt install apache2 php libapache2-mod-php mariadb-server -y", shell=True)
        except:
                print("erreur3")

def package2 ():
        try:
                package_name1 = "<php-mysqli><php-mbstring><php-curl><php-gd><php-simplexml><php-intl><php-ldap><php-apcu><php-xmlrpc><php-cas><php-zip><php-bz2><php-ldap><php-imap>"
                subprocess.run(["apt", "install", "-y", package_name1], check=True)

        except:
                print("erreur4")

#menu() 
telechargement(glpiUrl, downloadFile)
untar(downloadFile, extractDir)
package()
