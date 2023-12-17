# Variables numériques : boxplots

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

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

# Chargement des données
df = pd.read_csv("stackoverflow_full.csv")

# Recodage des variables catégorielles (ENG -> FR)
df_fr = df.copy()

df_fr["EmployedCat"] = pd.cut(df_fr["Employed"], bins=[-1, 0, 1], labels=["Sans emploi", "En emploi"]).astype("object")

df_fr["Age"] = df_fr["Age"].replace(
    ["<35", ">35"],
    ["Moins de 35 ans", "Plus de 35 ans"]
)

df_fr["Accessibility"] = df_fr["Accessibility"].replace(
    ["No", "Yes"],
    ["Non", "Oui"]
)

df_fr["EdLevel"] = df_fr["EdLevel"].replace(
    ["NoHigherEd", "Undergraduate", "Master", "PhD", "Other"],
    ["Pas d'éducation supérieure", "Licence", "Master", "Doctorat", "Autre"]
)

df_fr["Gender"] = df_fr["Gender"].replace(
    ["Man", "Woman", "NonBinary"],
    ["Homme", "Femme", "Non-Binaire"]
)

df_fr["MentalHealth"] = df_fr["MentalHealth"].replace(
    ["No", "Yes"],
    ["Non", "Oui"]
)

df_fr["MainBranch"] = df_fr["MainBranch"].replace(
    ["Dev", "NotDev"],
    ["Développement", "Autre"]
)

# Salaire précédent vs. statut d'emploi
fig_salaire = px.box(df_fr, x="EmployedCat", y = "PreviousSalary")

fig_salaire.update_layout(
    title_text="Distribution du salaire précédent selon le statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Salaire précédent",
    bargap=0.2, 
    bargroupgap=0.1 
)

# Compétences en informatique vs. statut d'emploi
fig_info = px.box(df_fr, x="EmployedCat", y = "ComputerSkills")

fig_info.update_layout(
    title_text="Distribution des compétences en informatique selon le statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Compétences en informatique",
    bargap=0.2, 
    bargroupgap=0.1 
)

# Années de code pro vs. statut d'emploi
fig_codepro = px.box(df_fr, x="EmployedCat", y = "YearsCodePro")

fig_codepro.update_layout(
    title_text="Distribution des années de code professionnel selon le statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Années de code professionnel",
    bargap=0.2, 
    bargroupgap=0.1 
)

# Années de code vs. statut d'emploi
fig_code = px.box(df_fr, x="EmployedCat", y = "YearsCode")

fig_code.update_layout(
    title_text="Distribution des années de code selon le statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Années de code",
    bargap=0.2, 
    bargroupgap=0.1 
)

# Choix du graphe
tab_salaire, tab_info, tab_codepro, tab_code = st.tabs(["Salaire précédent", "Compétences en informatique", "Années de code professionnel", "Années de code"])

with tab_salaire:
    st.plotly_chart(fig_salaire)
with tab_info:
    st.plotly_chart(fig_info)
with tab_codepro:
    st.plotly_chart(fig_codepro)
with tab_code:
    st.plotly_chart(fig_code)

st.markdown(
    """
    On remarque donc que ...
    """
)
