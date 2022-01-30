import search_veloMag as vmag
import calcule as clc
import search_park as park


def ressort_global():

    vmag_total_average = []
    vmag_total_standard_scratch = []

    park_total_average = []
    park_total_standard_scratch = []

    for i in range (17,22):
        print("01-"+ str(i) )
        y = (vmag.csv_file_reader_per_month_and_day_by_hour("stat_vmag.csv","01-"+str(i),["free_vmag_space","total_vmag_space"]))
        
        x = (vmag.csv_file_reader_per_month_and_day_by_hour("stat_park.csv","01-"+str(i),["free_park_space","total_park_space"]))

        for j in range(24):
            
            try:
                for k in range (len(y[j])):
                    
                    vmag_total_average.append(clc.average(vmag.average_occupied(y[j][k])))
                    vmag_total_standard_scratch.append(clc.standard_scratch(vmag.average_occupied(y[j][k])))
                    
            except IndexError:
                pass

            for k in range (len(x[j])):
                park_total_average.append(clc.average(vmag.average_occupied(x[j][k])))
                park_total_standard_scratch.append(clc.standard_scratch(vmag.average_occupied(x[j][k])))

    vmag_total_average = round(clc.average(vmag_total_average)/100,2)
    vmag_total_standard_scratch = round(clc.average(vmag_total_standard_scratch)/100,2)

    park_total_average = round(clc.average((park_total_average))/100,2)
    park_total_standard_scratch = round(clc.average((park_total_standard_scratch))/100,2)

    print(f"Vmag moyenne global : {vmag_total_average}")
    print(f"Vmag écart-type global : {vmag_total_standard_scratch}")

    print(f"Park moyenne global : {park_total_average}")
    print(f"Park écart-type global : {park_total_standard_scratch}")


def dat_file():


    vmag_total_average = []
    park_total_average = []

    file_name = "data.dat"

    file = open(file_name,'w',encoding='utf8') # ouvre le fichier en mode écriture ( si inexistant : création file )

    header = "#Day.Hour #Vmag% #Park%\n"
    file.write(header)                           # écrit dans le fichier le contenu de la page web

    
    for i in range (17,22):
        print("01-"+ str(i) )
        y = (vmag.csv_file_reader_per_month_and_day_by_hour("stat_vmag.csv","01-"+str(i),["free_vmag_space","total_vmag_space"]))
        
        x = (vmag.csv_file_reader_per_month_and_day_by_hour("stat_park.csv","01-"+str(i),["free_park_space","total_park_space"]))

        for j in range(24):
            
            try:
                for k in range (len(y[j])):
                   
                    vmag_total_average.append(clc.average(vmag.average_occupied(y[j][k])))
                    
            except IndexError:
                pass
            
            for k in range (len(x[j])):

                park_total_average.append(clc.average(vmag.average_occupied(x[j][k])))

            content_vmag = round(clc.average(vmag_total_average)/100,2)
            content_park = round(clc.average(park_total_average)/100,2)
            
            try:
                content_to_write = f"{y[j][0][2][3:5]}.{y[j][0][3][0:2]} {content_vmag} {content_park}\n"
                file.write(content_to_write)
            except IndexError:
                continue

    file.close()                                  # ferme proprement le fichier

ressort_global()

dat_file()

