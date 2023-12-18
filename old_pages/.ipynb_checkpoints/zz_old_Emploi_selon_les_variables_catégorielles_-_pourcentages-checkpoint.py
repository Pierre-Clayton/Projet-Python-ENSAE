# Variables catégorielles : pourcentages

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

st.set_page_config(
    page_title="Variables catégorielles : pourcentages", 
    page_icon=":chart_with_upwards_trend:"
)

st.markdown(
    """
    ## Variables catégorielles : pourcentages

    On étudie ici la distribution des quatre principales variables catégorielles : l'âge, le genre, le niveau d'éducation et la branche professionnelle principale, selon le statut d'emploi.
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
# DF des Pourcentages Age
grouped_df_age = df_fr.groupby(['Age', 'EmployedCat']).size().reset_index(name='count')
total_counts = df_fr.groupby('EmployedCat').size()

grouped_df_age['percentage'] = (grouped_df_age['count'] / grouped_df_age['EmployedCat'].map(total_counts) * 100).round(1)

# Graphe Pourcentages Age
fig_age = px.bar(grouped_df_age, orientation = 'h', x="percentage", y = "EmployedCat", color = "Age", text_auto = True)

fig_age.update_layout(
    title_text="Distribution de l'âge selon le statut d'emploi",
    xaxis_title_text="Pourcentage", 
    yaxis_title_text="Statut d'emploi",
    legend_title_text = "Age",
    bargap=0.2, 
    bargroupgap=0.1 
)

fig_age.update_traces(texttemplate = '%{x}%')

# 2. Graphe Genre
# DF des Pourcentages Genre
grouped_df_genre = df_fr.groupby(['Gender', 'EmployedCat']).size().reset_index(name='count')

grouped_df_genre['percentage'] = (grouped_df_genre['count'] / grouped_df_genre['EmployedCat'].map(total_counts) * 100).round(1)

# Graphe Pourcentages Genre
fig_genre = px.bar(grouped_df_genre, orientation = 'h', x="percentage", y = "EmployedCat", color = "Gender", text_auto = True)

fig_genre.update_layout(
    title_text="Distribution du genre selon le statut d'emploi",
    xaxis_title_text="Pourcentage", 
    yaxis_title_text="Statut d'emploi",
    legend_title_text = "Genre",
    bargap=0.2, 
    bargroupgap=0.1 
)

fig_genre.update_traces(texttemplate = '%{x}%')

# 3. Graphe Niveau d'éducation
# DF des Pourcentages Niveau d'éd
grouped_df_ed = df_fr.groupby(['EdLevel', 'EmployedCat']).size().reset_index(name='count')

grouped_df_ed['percentage'] = (grouped_df_ed['count'] / grouped_df_ed['EmployedCat'].map(total_counts) * 100).round(1)

# Graphe Pourcentages Niveau d'éd
fig_ed = px.bar(grouped_df_ed, orientation = 'h', x="percentage", y = "EmployedCat", color = "EdLevel", text_auto = True,
                category_orders = dict(EdLevel = ["Pas d'éducation supérieure", "Licence", "Master", "Doctorat", "Autre"])
)

fig_ed.update_layout(
    title_text="Distribution du niveau d'éducation selon le statut d'emploi",
    xaxis_title_text="Pourcentage", 
    yaxis_title_text="Statut d'emploi",
    legend_title_text = "Niveau d'éducation",
    bargap=0.2, 
    bargroupgap=0.1 
)

fig_ed.update_traces(texttemplate = '%{x}%')

# 4. Graphe Branche pro
# DF des Pourcentages Branche pro
grouped_df_branch = df_fr.groupby(['MainBranch', 'EmployedCat']).size().reset_index(name='count')

grouped_df_branch['percentage'] = (grouped_df_branch['count'] / grouped_df_branch['EmployedCat'].map(total_counts) * 100).round(1)

# Graphe Pourcentages Branche pro
fig_branch = px.bar(grouped_df_branch, orientation = 'h', x="percentage", y = "EmployedCat", color = "MainBranch", text_auto = True,
                    category_orders = dict(MainBranch = ["Développement", "Autre"])
                   )

fig_branch.update_layout(
    title_text="Distribution de la branche professionnelle selon le statut d'emploi",
    xaxis_title_text="Pourcentage", 
    yaxis_title_text="Statut d'emploi",
    legend_title_text = "Branche professionnelle principale",
    bargap=0.2, 
    bargroupgap=0.1 
)

fig_branch.update_traces(texttemplate = '%{x}%')

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
