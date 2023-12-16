# Variables catégorielles : histogrammes

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Variables catégorielles : histogrammes", 
    page_icon=":chart_with_upwards_trend:"
)

st.markdown(
    """
    ## Variables catégorielles : histogrammes

    On étudie ici la distribution du statut d'emploi selon les quatre principales variables catégorielles : l'âge, le genre, le niveau d'éducation et la branche professionnelle principale.
    """
)

df = pd.read_csv("stackoverflow_full.csv")

# Configuration des paramètres de visualisation
sns.set(style="whitegrid")

# Tracé des distributions des colonnes démographiques clés et de leur relation avec le statut 'Employed'
# Âge vs. Employé
fig = plt.figure(figsize=(4, 5))
sns.histplot(data = df, x="Age", hue="Employed", multiple = "dodge", shrink=.8)
plt.title("Distribution de l'âge vs. Statut d'emploi")
plt.xlabel("Âge", fontsize=10)
plt.ylabel(" ")
st.pyplot(fig.get_figure())

# Genre vs. Employé
fig = plt.figure(figsize=(4, 5))
sns.histplot(data=df, x="Gender", hue="Employed", multiple = "dodge", shrink=.8)
plt.title("Distribution du genre vs. Statut d'emploi")
plt.xlabel("Genre", fontsize=10)
plt.ylabel(" ")
st.pyplot(fig.get_figure())

# Niveau d'éducation (EdLevel) vs. Employé
fig = plt.figure(figsize=(4, 5))
sns.histplot(data=df, x="EdLevel", hue="Employed", multiple = "dodge", shrink=.8)
plt.title("Niveau d'éducation vs. Statut d'emploi")
plt.xlabel("Niveau d'éducation", fontsize=10)
plt.ylabel(" ")
plt.xticks(rotation=45)
st.pyplot(fig.get_figure())

# Branche principale (MainBranch) vs. Employé
fig = plt.figure(figsize=(4, 5))
sns.histplot(data=df, x="MainBranch", hue="Employed", multiple = "dodge", shrink=.8)
plt.title("Branche professionnelle principale vs. Statut d'emploi")
plt.xlabel("Branche professionnelle principale", fontsize=10)
plt.ylabel(" ")
st.pyplot(fig.get_figure())


