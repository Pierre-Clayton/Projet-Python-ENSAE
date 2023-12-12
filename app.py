import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fonction principale de l'application Streamlit
def main():
    st.title("Mon Application Streamlit pour la Visualisation des Données")

    # Chargement des données (remplacez ceci par le chemin de votre fichier)
    data = pd.read_csv("stackoverflow_full.csv")

    # Affichage des données dans l'application
    st.write("Aperçu des données :")
    st.write(data.head())

    # Création d'un graphique simple (ajustez selon vos données)
    st.write("Visualisation des données :")
    fig, ax = plt.subplots()
    ax.hist(data['YearsCode'], bins=20)
    st.pyplot(fig)

# Exécution de la fonction principale
if __name__ == "__main__":
    main()
