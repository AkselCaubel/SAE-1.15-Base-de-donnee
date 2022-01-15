########################
# CALCULE MATHEMATIQUE #
########################

from math import sqrt


def moyenne(liste):
    """ Renvois la moyenne d'une liste d'int"""
    return round(sum(liste)/len(liste),2)

def ecart_type(liste):
    """ Renvois l'écart type d'une liste d'int"""
    moy = moyenne(liste)
    result = 0

    for i in range (len(liste)):

        result += (liste[i] - moy)**2
    return round(sqrt(result/len(liste)),2)

    """ Save """

"""def ecart_type(data,moyenne):
     calcule l'écart type des données et le renvois 

    content = csv_file_reader(data)  # récupère le contenu de de data_file ( type = list )
    result = 0                            # initialisation du résultat de la moyenne ( type = int )
    compteur = 0                          # initialisation du compteur d'élément 
    
    for i in range (len(content)):                            # pour toute les rangées de content faire
        result += (int(content[i][2]) - int(content[i][1]) - moyenne)**2     # result prend le nombre de place occupée
        compteur += 1                                         # incrémentation du compteur
        
    return round(sqrt(result/compteur))"""