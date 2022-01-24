from time import sleep
import threading as th 

import search_park as park
import search_veloMag as vmag
import scraping as scp

def VeloMag():
    vmag.writer(scp.web_content(id[24]),"vmag","w",".xml")
    vmag.csv_file_writer_parse(scp.xml_vmag_parse("./station_file/vmag.xml"),csv_existe)

def Parking():
    park.csv_file_writer_parse(id[0:23],csv_existe)

def existe_file():
    global csv_existe

    sleep(60)
    csv_existe = True


id = ["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO", # Identifiant de chaque parking. L'on aurait pu les récupérés automatiquement
      "FR_MTP_FOCH","FR_MTP_GAMB","FR_MTP_GARE","FR_MTP_TRIA", # mais pour le peu de parking celà aurait pris plus de temps pour rien
      "FR_MTP_ARCT","FR_MTP_PITO","FR_MTP_CIRC","FR_MTP_SABI",
      "FR_MTP_GARC","FR_MTP_SABL","FR_MTP_MOSS","FR_STJ_SJLC",
      "FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109",
      "FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE","FR_MTP_POLY",
      "TAM_MMM_VELOMAG"]



"""th3 = th.Thread(target=existe_file)

i=0
csv_existe = False
th3.start()

while i<=2016:
    th1 = th.Thread(target=VeloMag)
    th2 = th.Thread(target=Parking)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    sleep(60*1)
    i+=1"""

print(park.average_occupied('stat_park.csv'))
print(park.standard_scratch_occupied('stat_park.csv',park.average_occupied('stat_park.csv')))



