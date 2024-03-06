import pandas as pd

import numpy as np


def calculer_distance_totale(solution, distances):
    """
    Fonction pour calculer la distance totale d'une solution.
    """
    distance_totale = 0
    for i in range(len(solution) - 1):
        distance_totale += distances[solution[i]][solution[i+1]]
    # Ajouter la distance entre la dernière ville et la première ville pour compléter la boucle.
    distance_totale += distances[solution[-1]][solution[0]]
    return distance_totale

def forte_descente(distances):
    """
    Algorithme de forte descente avec la méthode de 2 échanges.
    """
    nb_villes = len(distances)
    solution_actuelle = list(range(nb_villes))  # Solution initiale
    distance_actuelle = calculer_distance_totale(solution_actuelle, distances)

    amelioration = True
    while amelioration:
        amelioration = False
        for i in range(nb_villes):
            for j in range(i+1, nb_villes):
                nouvelle_solution = solution_actuelle.copy()
                nouvelle_solution[i], nouvelle_solution[j] = nouvelle_solution[j], nouvelle_solution[i]
                nouvelle_distance = calculer_distance_totale(nouvelle_solution, distances)
                if nouvelle_distance < distance_actuelle:
                    solution_actuelle = nouvelle_solution
                    distance_actuelle = nouvelle_distance
                    amelioration = True
                    break
            if amelioration:
                break

    return solution_actuelle, distance_actuelle

# Exemple d'utilisation



# Chemin vers le fichier Excel
chemin_fichier_excel = "C://Users//O//Desktop//distance.xlsx"

# Lire le fichier Excel
donnees_excel = pd.read_excel(chemin_fichier_excel)
donnees = donnees_excel.values
# Afficher les premières lignes du fichier Excel

 # Appliquer l'algorithme de forte descente
meilleure_solution, distance_minimale = forte_descente(donnees)
print("Meilleure solution:", meilleure_solution)
print("Distance minimale:", distance_minimale)
