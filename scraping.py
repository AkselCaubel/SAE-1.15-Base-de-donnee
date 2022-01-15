################
# WEB SCRAPING #
################


import requests
from lxml import etree

def web_content(id):

    """ renvois le contenu de la page rechercher a partir de l'ip du parking rechercher """

    base_url = "https://data.montpellier3m.fr/sites/default/files/ressources/" # partie de l'url qui ne change pas selon le parking
    extention_url = ".xml" # extension des fichiers d'information
    url = base_url+id+extention_url # rassemblement de l'url complete en fonction de du parking rechercher
    
    
    r = requests.get(url) # de la page internet
    content = r.text # contenu de la page

    return content


def xml_vmag_trie(xml_path_file):
    """ fonction qui parse le xml"""
    
    result = [] # initialisation de la variable de retour
    #xml_path_file=str

    tree = etree.parse(xml_path_file) # on initialise l'arboressence du fichier
    
    for si in tree.xpath("/vcs/sl/si"): # pour toutes les balises <si> se trouvant encapsulé dans /vcs/sl/
        one_station=[]                  # initialisation / reset de la liste contenant les infomations d'une station

        one_station.append(si.get("na"))  # prend le nom de la station
        one_station.append(si.get("av"))  # prend le nombre de vélo en circulation de la station
        one_station.append(si.get("fr"))  # prend le nombre de vélo libre de la station
        one_station.append(si.get("to"))  # prend le nombre total de vélo de la station

        result.append(one_station)        # prend les informations de chaque station sous forme de liste de liste

    return result   # renvois sous forme de liste de liste le fichier parsé