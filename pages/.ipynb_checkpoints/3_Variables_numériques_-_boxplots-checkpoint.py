# Variables numériques : boxplots

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic
from wordcloud import WordCloud

st.set_page_config(
    page_title="Variables numériques : boxplots", 
    page_icon=":chart_with_upwards_trend:"
)

st.markdown(
    """
    ## Variables numériques : boxplots

    On étudie ici la distribution des quatre principales variables numériques selon le statut d'emploi.
    """
)

df = pd.read_csv("stackoverflow_full.csv")

sns.set(style="whitegrid")

# Emploi vs. salaire précédent
fig = plt.figure(figsize=(4, 5))
sns.boxplot(x="Employed", y="PreviousSalary", data=df)
plt.title("Salaire précédent par statut d'emploi")
plt.xlabel("Statut d'emploi", fontsize=10)
plt.ylabel("Salaire précédent", fontsize=10)
st.pyplot(fig.get_figure())

# Emploi vs. compétences en informatique
fig = plt.figure(figsize=(4, 5))
sns.boxplot(x="Employed", y="ComputerSkills", data=df)
plt.title("Compétences en informatique par statut d'emploi")
plt.xlabel("Statut d'emploi", fontsize=10)
plt.ylabel("Compétences en informatique", fontsize=10)
st.pyplot(fig.get_figure())

# Emploi vs. années de code pro
fig = plt.figure(figsize=(4, 5))
sns.boxplot(x="Employed", y="YearsCodePro", data=df)
plt.title("Années de codage professionnel par statut d'emploi")
plt.xlabel("Statut d'emploi", fontsize=10)
plt.ylabel("Années de codage professionnel", fontsize=10)
st.pyplot(fig.get_figure())

# Emploi vs. années de code
fig = plt.figure(figsize=(4, 5))
sns.boxplot(x="Employed", y="YearsCode", data=df)
plt.title("Années de codage par statut d'emploi")
plt.xlabel("Statut d'emploi", fontsize=10)
plt.ylabel("Années de codage", fontsize=10)
st.pyplot(fig.get_figure())
