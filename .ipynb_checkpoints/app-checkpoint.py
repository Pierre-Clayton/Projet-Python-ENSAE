# Script principal d'appel de l'application

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from scriptspages import ST_PAGES
# ST_PAGES contient les références des script de chacune des pages

# Fonction principale de l'application Streamlit
def main():
    st.title("Visualisation des Données")

    # Création d'une barre latérale de navigation entre les pages de graphiques
    ## A noter : possible de faire 2 niveaux de choix si l'on souhaite
    with st.sidebar:
        st.header("Navigation")

        page_options = (
            list(ST_PAGES.keys())
        )
        
        selected_page = st.selectbox(
            label="Choissisez la page que vous souhaitez consulter",
            options=page_options,
        )
        
        page = (
            ST_PAGES[selected_page]
        )

    page()


# Exécution de la fonction principale
if __name__ == "__main__":
    st.set_page_config(
        page_title="Visualisation des Données", page_icon=":chart_with_upwards_trend:"
    )
    main()
