import pandas as pd
import numpy as np
import mysql.connector

from base_donnee import *

def main():
    # On crée notre objet connexion mySQL
    connexion = Base_donnee()
    connexion.gen_connexion()
    connexion.creer_curseur()

    def slicer (liste, pourcentage):
        """
        Cette fonction découpe une liste A en liste B nestée
        remplie de petits bouts issus de la liste A. Le pourcentage
        de 0 à 1
        correspondra à la taille des listes nestées dans le resultat.
        
        Par exemple, 0.5 donnera une liste nestée contenant deux slices,
        0.1 donnera des slices d'une taille de 10% de la liste A, etc.
        """

        # Gestion du cas où l'on rentrerait 0 au lieu d'une taille valide de slice.
        if pourcentage == 0:
            pourcentage +=1
            print("Le pourcentage ne doit pas être nul. Pourcentage repassé à 1.")
        
        resultat = []
        taille_liste = len(liste)

        taille_slices = taille_liste * pourcentage
        
        # variable qui fait la navette entre la liste d'éléments et la liste de listes nestées pour la charger :
        navette = []
        i = 0

        while i < taille_liste:

            # Si groupe pas fini, on lui ajoute l'élément de rang i et on incrémente i.
            if len(navette) < taille_slices:
                navette.append(liste[i])
                i+=1

            # Si groupe a atteint la taille visée, on l'ajoute à la liste de groupes et on le vide.
            else:
                resultat.append(navette)
                navette = []

        # Ajout d'un éventuel dernier groupe réduit (+ rapide sans condition pour tester si un tel groupe existe).
        resultat.append(navette)

        return resultat

    def liste_to_tuple(df):
        print("1 :",len(df))
        df = np.array(df)
        print("2 :", len(df))
        liste = df.tolist()
        print("3 :", len(liste))
        for i in range(len(liste)):
            liste[i] = tuple(liste[i])
        return liste


    ###################
    # IMPORT DATATEST #
    ###################

    df = pd.read_csv("./data/athlete_events.csv")
    df2 = pd.read_csv("./data/noc_regions.csv")
    # merged = pd.merge(df, df2, on='NOC', how="left")
    


    ###############
    # INJECTIONS  #
    ###############

    # Remplissage table nocs :

    liste_NOC = df2[["NOC", "region", "notes"]]
    liste_NOC = liste_NOC.fillna("nan")

    liste_NOC = liste_to_tuple(liste_NOC)
    liste_NOC = list(set(liste_NOC))

    # ajout d'un NOC qui manquait pour Singapour :
    liste_NOC.append(("SGP", "Singapore", "nan"))
    
    liste_NOC = slicer(liste_NOC, 0.5)

    for i in liste_NOC:
        connexion.injecter_nocs(i)
    
    # Remplissage table équipes :

    liste_equipes = df[["Team","NOC"]]

    liste_equipes = liste_to_tuple(liste_equipes)
    liste_equipes = list(set(liste_equipes))

    liste_equipes = slicer(liste_equipes, 0.2)

    for i in liste_equipes :
        connexion.injecter_equipes(i)


    # Remplissage table athletes :
    liste_athletes = df[["ID","Name","Sex"]]
    liste_athletes = liste_to_tuple(liste_athletes)
    liste_athletes = list(set(liste_athletes))

    liste_athletes = slicer(liste_athletes, 0.2)
    
    for i in liste_athletes :
        connexion.injecter_athletes(i)

    # Remplissage table jeux :
    liste_jeux = df[["Games", "Year", "Season"]]

    liste_jeux = liste_to_tuple(liste_jeux)
    liste_jeux = list(set(liste_jeux))
    
    liste_jeux = slicer(liste_jeux, 0.2)
    for i in liste_jeux :
        connexion.injecter_jeux(i)

    # Remplissage table sports :
    liste_sports = df[["Sport"]]

    liste_sports = liste_to_tuple(liste_sports)
    liste_sports = list(set(liste_sports))
    
    liste_sports = slicer(liste_sports, 0.2)
    for i in liste_sports :
        connexion.injecter_sports(i)


    # Remplissage table epreuves :
    liste_epreuves = df[["Event", "Sport"]]

    liste_epreuves = liste_to_tuple(liste_epreuves)
    liste_epreuves = list(set(liste_epreuves))
    
    liste_epreuves = slicer(liste_epreuves, 0.2)
    for i in liste_epreuves :
        connexion.injecter_epreuves(i)


    # Remplissage table intermédiaire epreuves_jeux :
    liste_epreuves_jeux = df[["Event", "Games", "Year", "Season"]]

    liste_epreuves_jeux = liste_to_tuple(liste_epreuves_jeux)
    liste_epreuves_jeux = list(set(liste_epreuves_jeux))
    
    liste_epreuves_jeux = slicer(liste_epreuves_jeux, 0.2)
    for i in liste_epreuves_jeux :
        connexion.injecter_epreuves_jeux(i)

    # Remplissage table villes :
    liste_villes = df[["City"]]

    liste_villes = liste_to_tuple(liste_villes)
    liste_villes = list(set(liste_villes))
    
    liste_villes = slicer(liste_villes, 0.01)
    for i in liste_villes :
        connexion.injecter_villes(i)

    # Remplissage table jeux_villes :
    liste_jeux_villes = df[["Games", "Year", "Season", "City"]]
    liste_jeux_villes = liste_to_tuple(liste_jeux_villes)
    liste_jeux_villes = list(set(liste_jeux_villes))
    

    liste_jeux_villes = slicer(liste_jeux_villes, 0.01)
    for i in liste_jeux_villes :
        connexion.injecter_jeux_villes(i)


    print(df[["ID", "Event", "Medal", "Age", "Weight", "Height"]].isna().sum())
    # On remplace les âges manquants par l'âge médian :
    df[["Age"]] = df[["Age"]].fillna(df[["Age"]].median())
    # On remplace les poids manquants par les poids médians :
    df[["Weight"]] = df[["Weight"]].fillna(df[["Weight"]].median())
    # On remplace les tailles manquantes par les tailles médianes :
    df[["Height"]] = df[["Height"]].fillna(df[["Height"]].median())
    # On remplace les médailles manquantes par la mension "aucune" :
    df[["Medal"]] = df[["Medal"]].fillna("aucune")
    print(df[["ID", "Event", "Medal", "Age", "Weight", "Height"]].isna().sum())

    # Remplissage de la table intermédiaire athletes_epreuves :
    liste_ath_epr = df[["ID", "Event", "Medal", "Age", "Weight", "Height"]]

    liste_ath_epr = liste_to_tuple(liste_ath_epr)
    liste_ath_epr = list(set(liste_ath_epr))

    liste_ath_epr = slicer(liste_ath_epr, 0.01)
    for i in liste_ath_epr :
        connexion.injecter_athletes_epreuves(i)

    # Remplissage table intermédiaire equipes_athletes :
    liste_equ_ath = df[["ID", "Team", "NOC"]]
    print(df[["ID", "Team", "NOC"]].isna().sum())

    liste_equ_ath = liste_to_tuple(liste_equ_ath)
    liste_equ_ath = list(set(liste_equ_ath))

    liste_equ_ath = slicer(liste_equ_ath, 0.05)
    for i in liste_equ_ath :
        connexion.injecter_equipes_athletes(i)

    # Remplissage table intermédiaire equipes_athletes :
    liste_ath_sports = df[["ID", "Sport"]]
    print(df[["ID", "Team", "NOC"]].isna().sum())

    liste_ath_sports = liste_to_tuple(liste_ath_sports)
    liste_ath_sports = list(set(liste_ath_sports))

    liste_ath_sports = slicer(liste_ath_sports, 0.05)
    for i in liste_ath_sports :
        connexion.injecter_athletes_sports(i)


    print("requêtes effectuées")
    connexion.fermer_curseur()
    print("curseur fermé")

main()