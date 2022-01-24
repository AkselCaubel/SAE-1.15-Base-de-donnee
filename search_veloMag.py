import csv
from time import sleep
from math import sqrt
from datetime import datetime
from copy import deepcopy

import log as lg




def writer(content,station_name="vmag",mode="w",extension=".txt"):
    """ Met le contenu de la page dans un fichier txt au nom de la station ( si pas de fichier : il le crée )"""


    file_name = "./station_file/"+station_name+extension # trouve le nom de la station puis rajoute l'extention .txt pour le fichier 

    fichier = open(file_name,mode,encoding='utf8') # ouvre le fichier en mode écriture ( si inexistant : création file )

    fichier.write(content)                           # écrit dans le fichier le contenu de la page web

    fichier.close()                                  # ferme proprement le fichier



def csv_file_writer_parse(info_station,csv_existe):
    #global csv_existe
    """" écrit dans le fichier stat_vmag.csv les données xml de manière ordonée"""

    time = str(datetime.now())

    with open('stat_vmag.csv', 'a', newline='') as csvfile:      # ouvre un fichier CSV en écriture nommée stat.csv ou le crée si existe pas
        
        fieldnames = ['station_name', 'taken_vmag_space','free_vmag_space','total_vmag_space','year','day&month','hour&min']     # donne les noms de chaque catégorie
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)                 # donne attirbut csv et les sépatateurs a la variable writer

        if csv_existe == False :    # Si le fichier csv est défini dans le main comme non existant ALORS
            writer.writeheader()    # On écrit le titre des catégories +
            csv_existe = True       # On défini dans le main le fichier comme existant 

        for i in range (len(info_station)):   # pour chaque id ( parking ) l'on écrit dans le fichier csv pour chaque catégorie leurs entrées
            writer.writerow({'station_name': info_station[i][0],'taken_vmag_space': info_station[i][1] , 'free_vmag_space': info_station[i][2], 'total_vmag_space': info_station[i][3],  'year': time[0:4],  'day&month': time[5:10],  'hour&min': time[11:16]})   # écrit dans le fichier csv

    lg.log_write(f"Une donnée a été enregisté dans le fichier stat_vmag.csv le {time[5:10]} à {time[11:16]} prochain relever prévu a {time[11:13]}:{str(int(time[14:16])+10)}")

def csv_file_reader_per_month_and_day_by_hour(file,day):

    """Fonction lisant un fichier csv ( file ) et retourne sous forme de liste tous les élément du fichier"""

    result = [] # ( type list )
    liste_tmp = []
    with open(file, newline='') as csvfile:   # ouvre un fichier 
        reader = csv.DictReader(csvfile)      
    
        tmp_hour = "00"

        
        for row in reader:

            print(tmp_hour,row['hour&min'][0:2])
            if day == row['day&month']:
            
                if tmp_hour == row['hour&min'][0:2]:
                    print("yes")
                    liste_tmp.append([row['station_name'],row['free_vmag_space'],row['total_vmag_space']])

                else:

                    result.append(deepcopy(liste_tmp))
                    liste_tmp = []

                    if len(str(int(tmp_hour)+ 1)) == 1:
                        tmp_hour = tmp_hour[0:1]+str(int(tmp_hour[1:])+1)

                    else:
                        tmp_hour=str(int(tmp_hour)+1)

        return result

    """        ###################
            print(row['hour&min'][0:2])

            if row['hour&min'][0:2] == tmp_hour :
                result.append([row['station_name'],row['free_vmag_space'],row['total_vmag_space']])
            else:
                if len(str(int(tmp_hour)+ 1)) == 1:
                    tmp_hour = tmp_hour[0:1]+str(int(tmp_hour[1:])+1)
                else:
                    tmp_hour=str(int(tmp_hour)+1)

    return result # type(list)"""