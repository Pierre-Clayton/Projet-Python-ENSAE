# Script principal d'appel de l'application

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from graphes import ST_GRAPHES
# ST_GRAPHES contient les références des fonctions de production de chacun des graphes

# Fonction principale de l'application Streamlit
def main():
    st.title("Visualisation des Données")

    # Chargement des données
    data = pd.read_csv("stackoverflow_full.csv")

    # Affichage des données dans l'application
    st.write("Aperçu des données :")
    st.write(data.head())

    # Création d'un graphique simple (ajustez selon vos données)
    st.write("Visualisation des données :")
    fig, ax = plt.subplots()
    ax.hist(data['YearsCode'], bins=20)
    st.pyplot(fig)

    # Création d'une barre latérale de navigation entre les pages de graphiques
    ## A noter : possible de faire 2 niveaux de choix si l'on souhaite
    with st.sidebar:
        st.header("Navigation")

        page_options = (
            list(ST_GRAPHES.keys())
        )
        
        selected_page = st.selectbox(
            label="Choissisez un graphique",
            options=page_options,
        )
        
        graphe = (
            ST_GRAPHES[selected_page]
        )

    graphe()


# Exécution de la fonction principale
if __name__ == "__main__":
    st.set_page_config(
        page_title="Visualisation des Données", page_icon=":chart_with_upwards_trend:"
    )
    main()
