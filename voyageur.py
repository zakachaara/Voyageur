pip install openpyxl
import pandas as pd
import streamlit as st
import pandas as pd


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

# Afficher un champ pour télécharger un fichier Excel
fichier_excel = st.file_uploader("Télécharger votre fichier Excel", type=['xlsx'])

if fichier_excel is not None:
    # Lire le fichier Excel
    donnees_excel = pd.read_excel(fichier_excel)

    # Transformer les données en un tableau numpy
    donnees = donnees_excel.values

    # Maintenant, vous pouvez utiliser votre tableau numpy (donnees_numpy) comme bon vous semble
    st.write("Données lues à partir du fichier Excel :")
    st.write(donnees_excel)
     # Appliquer l'algorithme de forte descente
    meilleure_solution, distance_minimale = forte_descente(donnees)
    st.write("Meilleure solution:", meilleure_solution)
    st.write("Distance minimale:", distance_minimale)
    st.write("By Zakaria CHAARA")


