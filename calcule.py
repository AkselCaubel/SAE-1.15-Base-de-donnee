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

