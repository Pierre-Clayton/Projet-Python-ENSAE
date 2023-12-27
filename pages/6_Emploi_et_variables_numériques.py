# Emploi et variables numériques : boxplots

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

st.set_page_config(
    page_title="Emploi et variables numériques", 
    page_icon=":chart_with_upwards_trend:"
)

with st.sidebar:
    st.title("Projet Python pour la Data Science")
    st.subheader("Pierre CLAYTON")
    st.subheader("Clément DE LARDEMELLE")
    st.subheader("Louise LIGONNIERE")

st.markdown(
    """
    ## Emploi et variables numériques

    On étudie ici la distribution des quatre principales variables numériques selon le statut d'emploi.
    """
)

# Chargement des données
df = pd.read_csv("stackoverflow_full.csv")

# Recodage des variables catégorielles (ENG -> FR)
df_fr = df.copy()

df_fr["EmployedCat"] = pd.cut(df_fr["Employed"], bins=[-1, 0, 1], labels=["Sans emploi", "En emploi"]).astype("object")

# 1. Années de code vs. statut d'emploi
fig_code = px.box(df_fr, x="EmployedCat", y = "YearsCode")

fig_code.update_layout(
    title_text="Distribution des années de code selon le statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Années de code",
    bargap=0.2, 
    bargroupgap=0.1 
)

# 2. Années de code pro vs. statut d'emploi
fig_codepro = px.box(df_fr, x="EmployedCat", y = "YearsCodePro")

fig_codepro.update_layout(
    title_text="Distribution des années de code professionnel selon le statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Années de code professionnel",
    bargap=0.2, 
    bargroupgap=0.1 
)

# 3. Salaire précédent vs. statut d'emploi
fig_salaire = px.box(df_fr, x="EmployedCat", y = "PreviousSalary")

fig_salaire.update_layout(
    title_text="Distribution du salaire précédent selon le statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Salaire précédent",
    bargap=0.2, 
    bargroupgap=0.1 
)

# 4. Compétences en informatique vs. statut d'emploi
fig_info = px.box(df_fr, x="EmployedCat", y = "ComputerSkills")

fig_info.update_layout(
    title_text="Distribution des compétences en informatique selon le statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Compétences en informatique (nombre de langages maîtrisés)",
    bargap=0.2, 
    bargroupgap=0.1 
)

# Choix du graphe
tab_code, tab_codepro, tab_salaire, tab_info = st.tabs(["Années de code", "Années de code professionnel", "Salaire précédent", "Compétences en informatique"])

with tab_code:
    st.plotly_chart(fig_code)
with tab_codepro:
    st.plotly_chart(fig_codepro)
with tab_salaire:
    st.plotly_chart(fig_salaire)
with tab_info:
    st.plotly_chart(fig_info)

st.markdown(
    """
    On remarque donc que ...
    """
)
