# Langages utilisés

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(
    page_title="Langages utilisés", 
    page_icon=":chart_with_upwards_trend:"
)

with st.sidebar:
    st.title("Projet Python pour la Data Science")
    st.subheader("Pierre CLAYTON")
    st.subheader("Clément DE LARDEMELLE")
    st.subheader("Louise LIGONNIERE")

st.markdown(
    """
    ## Langages utilisés par les répondants

    """
)

# Chargement des données
df = pd.read_csv("stackoverflow_full.csv")

# Travailler avec HaveWorkedWith avant de supprimer la colonne
x = [str(cat).split(";") for cat in df["HaveWorkedWith"]]
texte = [item for sublist in x for item in sublist]
texte_final = "".join(cat for cat in texte)

# Création d'un nuage de mots avec le texte en tant qu'argument dans la méthode .generate()
nuage_de_mots = WordCloud(collocations=False, background_color='white').generate(texte_final)

# Afficher le nuage de mots généré
fig, ax = plt.subplots(figsize = (12, 8))
ax.imshow(nuage_de_mots)
plt.axis("off")
st.pyplot(fig)

st.markdown(
    """
    On remarque donc que ...
    """
)
