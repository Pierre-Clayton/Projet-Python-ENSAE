# Page d'accueil de l'application

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Visualisation des Données", 
    page_icon=":chart_with_upwards_trend:"
)

st.markdown(
    """
    # Bienvenue sur l'application de visualisation des données !

    Ce projet s'appuie sur l'édition 2022 de l'enquête annuelle générée par les utilisateurs de StackOverflow, qui s'intéresse à tous les aspects de l'expérience des développeurs, de l'apprentissage du code aux technologies préférées, en passant par le contrôle de version et l'expérience professionnelle. L'enquête réunit les réponses de plus de 70 000 utilisateurs, issus de plus de 180 pays.
    
    À partir des résultats de l'enquête, nous avons construit un jeu de données avec les colonnes suivantes :    
    - `Age` : âge du candidat, >35 ans ou <35 ans *(catégorique)*
    - `EdLevel` : niveau d'éducation du candidat (Licence, Master, Doctorat...) *(catégorique)*
    - `Gender` : genre du candidat (Homme, Femme, ou Non-Binaire) *(catégorique)*
    - `MainBranch` : si le candidat est un développeur professionnel *(catégorique)*
    - `YearsCode` : depuis combien de temps le candidat programme *(entier)*
    - `YearsCodePro` : depuis combien de temps le candidat programme dans un contexte professionnel *(entier)*
    - `PreviousSalary` : salaire du dernier emploi du candidat *(flottant)*
    - `ComputerSkills` : les compétences informatiques, mesurées par le nombre de langages maîtrisés par le candidat *(entier)*
    - `Employed` : variable cible, indiquant si le candidat est employé *(catégorique)*

    **Sélectionnez la page souhaitée dans la barre latérale** pour mieux comprendre les données utilisées dans ce projet.
    """
)
