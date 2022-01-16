import search_park as park
import search_veloMag as vmag
import scraping as scp
from time import sleep

id = ["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO", # Identifiant de chaque parking. L'on aurait pu les récupérés automatiquement
      "FR_MTP_FOCH","FR_MTP_GAMB","FR_MTP_GARE","FR_MTP_TRIA", # mais pour le peu de parking celà aurait pris plus de temps pour rien
      "FR_MTP_ARCT","FR_MTP_PITO","FR_MTP_CIRC","FR_MTP_SABI",
      "FR_MTP_GARC","FR_MTP_SABL","FR_MTP_MOSS","FR_STJ_SJLC",
      "FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109",
      "FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE","FR_MTP_POLY",
      "TAM_MMM_VELOMAG"]


demande_existe = input("le fichier csv existe ? ( 'y' pour oui autre pour non):")

if demande_existe.lower() == "yes":
    csv_existe = True
else : 
    csv_existe = False

#x = vmag.writer(scp.web_content(id[24]),station_name="vmag",mode="w",extension=".xml")
#print(scp.xml_vmag_trie("./station_file/vmag.xml"))


#xml_velo_trie = vmag.xml_trie(scp.web_content(id[24]))
#print(xml_velo_trie)


#print(vmag.writer(scp.web_content(id[24]),mode = "w"))
# mettre en commentaire la boucle pour afficher la moyenne et l'écart type du relevé 

i=0
while i<=2016:
    vmag.writer(scp.web_content(id[24]),"vmag","w",".xml")
    vmag.csv_file_writer_trie(scp.xml_vmag_trie("./station_file/vmag.xml"),csv_existe)
    park.csv_file_writer_trie(id[0:23],csv_existe)
    

    sleep(60*10)
    i+=1

print(park.moyenne_occupee('stat.csv'))
print(park.ecart_type_occupee('stat.csv',park.moyenne_occupee('stat.csv')))



