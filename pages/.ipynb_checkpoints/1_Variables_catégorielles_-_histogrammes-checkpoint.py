# Variables catégorielles : histogrammes

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

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

# 1. Graphe Age
fig_age = px.histogram(df_fr, x="Age", color = "EmployedCat", barmode="group", text_auto = True)

fig_age.update_layout(
    title_text="Distribution du statut d'emploi selon l'âge",
    xaxis_title_text='Age', 
    yaxis_title_text="",
    legend_title_text = "",
    bargap=0.2, 
    bargroupgap=0.1 
)

# 2. Graphe Genre
fig_genre = px.histogram(df_fr, x="Gender", color = "EmployedCat", barmode="group", text_auto = True)

fig_genre.update_layout(
    title_text="Distribution du statut d'emploi selon le genre",
    xaxis_title_text='Genre', 
    yaxis_title_text="",
    legend_title_text = "",
    bargap=0.2, 
    bargroupgap=0.1 
)

# 3. Graphe Niveau d'éducation
fig_ed = px.histogram(df_fr, x="EdLevel", color = "EmployedCat", barmode="group", 
                      text_auto = True, 
                      category_orders = dict(EdLevel = ["Pas d'éducation supérieure", "Licence", "Master", "Doctorat", "Autre"])
                     )

fig_ed.update_layout(
    title_text="Distribution du statut d'emploi selon le niveau d'éducation",
    xaxis_title_text="Niveau d'éducation", 
    yaxis_title_text="",
    legend_title_text = "",
    bargap=0.2, 
    bargroupgap=0.1 
)

# 4. Graphe Branche pro
fig_branch = px.histogram(df_fr, x="MainBranch", color = "EmployedCat", barmode="group", text_auto = True)

fig_branch.update_layout(
    title_text="Distribution du statut d'emploi selon la branche professionnelle",
    xaxis_title_text="Branche professionnelle (principale)", 
    yaxis_title_text="",
    legend_title_text = "",
    bargap=0.2, 
    bargroupgap=0.1 
)

# Choix du graphe
tab_age, tab_genre, tab_ed, tab_branch = st.tabs(["Age", "Genre", "Niveau d'éducation", "Branche professionnelle"])

with tab_age:
    st.plotly_chart(fig_age)
with tab_genre:
    st.plotly_chart(fig_genre)
with tab_ed:
    st.plotly_chart(fig_ed)
with tab_branch:
    st.plotly_chart(fig_branch)

st.markdown(
    """
    On remarque donc que ...
    """
)
