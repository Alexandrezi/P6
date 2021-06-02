import requests
import tarfile


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

#menu() 
telechargement(glpiUrl, downloadFile)
untar(downloadFile, extractDir)
