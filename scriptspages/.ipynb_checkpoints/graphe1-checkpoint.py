# Script pour générer le graphe 1

## A noter : possible de regrouper plusieurs graphes entre eux sur une même page. Par exemple si ils ont la même forme ou considèrent le même genre de données / les mêmes variables
## Dans ce cas : définir leurs fonctions les unes après les autres sur le même script de page : graphe 1(), graphe2()
## Dans le ST_PAGE : mettre plusieurs entrées. 
## Syntaxe : ST_PAGE1 = {"Page 1 : Graphe 1": graphe1, "Page 1 : Graphe 2": graphe2}
## Ensuite on aura bien toutes les entrées du ST_PAGE1 dans le ST_PAGES concaténé (dans __init__.py)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fonction qui permet de générer la page souhaitée (ici correspond au graphe1) : 
def graphe1():
    data = pd.read_csv("stackoverflow_full.csv")
    fig, ax = plt.subplots()
    ax.hist(data['YearsCode'], bins=20)
    st.pyplot(fig)

# ST_GRAPHE1 est un dictionnaire où l'on a le nom de la page et le nom de sa fonction
# Sert pour ensuite être intégré à la liste des pages dispos et être appelé dans app.py
ST_GRAPHE1 = {"Graphe 1": graphe1}