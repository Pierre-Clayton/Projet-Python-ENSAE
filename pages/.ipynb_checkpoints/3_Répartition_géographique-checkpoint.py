# Répartition géographique

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

st.set_page_config(
    page_title="Répartition géographique", 
    page_icon=":chart_with_upwards_trend:"
)

with st.sidebar:
    st.title("Projet Python pour la Data Science")
    st.subheader("Pierre CLAYTON")
    st.subheader("Clément DE LARDEMELLE")
    st.subheader("Louise LIGONNIERE")

st.markdown(
    """
    ## Répartition géographique des répondants

    On étudie ici la répartition géographique de deux variables : le nombre de développeurs ayant répondu à l'enquête, et le taux d'emploi.

    """
)

# Chargement des données
df = pd.read_csv("stackoverflow_full.csv")

# Ajout d'une colonne Code ISO (nécessaire pour les cartes)
iso = pd.read_excel("/home/onyxia/work/Projet-Python-ENSAE/" + "Liste-Excel-des-pays-du-monde.xlsx")

def countries_to_iso(country):
    name_countries = iso['Unnamed: 4']
    for i in range(len(name_countries)):
        if name_countries[i] == country:
            return iso.loc[i,'Unnamed: 1']
    list_missing_values = ['United Kingdom of Great Britain and Northern Ireland',
     'Russian Federation',
     'United States of America',
     'Netherlands',
     'Iran, Islamic Republic of...',
     'Hong Kong (S.A.R.)',
     'United Arab Emirates',
     'Bolivia',
     'Czech Republic',
     'The former Yugoslav Republic of Macedonia',
     'Venezuela, Bolivarian Republic of...',
     'Dominican Republic',
     'Syrian Arab Republic',
     'Taiwan',
     'South Korea',
     'Republic of Moldova',
     "Lao People's Democratic Republic",
     'Democratic Republic of the Congo',
     'Philippines',
     'United Republic of Tanzania',
     'Kosovo',
     'Nomadic',
     'Congo, Republic of the...',
     'Republic of Korea',
     'Swaziland',
     'Libyan Arab Jamahiriya',
     'Sudan',
     'Palestine',
     'Cape Verde',
     'Niger',
     'Gambia']
    fixed_missing_values = ["GBR",
                    "RUS",
                    "USA",
                    "NLD",
                    "IRN",
                    "HKG",
                    "ARE",
                    "BOL",
                    "CZE",
                    "MKD",
                    "VEN",
                    "DOM",
                    "SYR",
                    "TWN",
                    "KOR",
                    "MDA",
                    "LAO",
                    "COG",
                    "PHL",
                    "TZA",
                    "XXK",
                    None,
                    "COG",
                    "KOR",
                    "SWZ",
                    "LBY",
                    "SDN",
                    "PSE",
                    "CPV",
                    "NER",
                    "GMB"]
    for i in range(len(list_missing_values)):
        if list_missing_values[i] == country:
            return fixed_missing_values[i]
        
df['ISO'] = df['Country'].apply(countries_to_iso)

# Tableau nombre de répondants et taux d'emploi par pays
df_carto = df.groupby(['Country','ISO'])['Employed'].agg(['count', 'mean']).reset_index()
df_carto.columns = ['Country', 'ISO', 'count', 'percentage']
df_carto['percentage'] *= 100

# 1. Carte du nb de développeurs
fig_nb = px.choropleth(df_carto, locations="ISO",
                    color="count",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma)

fig_nb.update_layout(
    title_text="Nombre de répondants par pays",
    coloraxis_colorbar_title_text = "Effectif",
)

# 2. Carte du taux d'emploi
fig_taux = px.choropleth(df_carto, locations="ISO",
                    color="percentage",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma)

fig_taux.update_layout(
    title_text="Taux d'emploi par pays",
    coloraxis_colorbar_title_text = "Taux d'emploi",
)

# Choix du graphe
tab_nb, tab_taux = st.tabs(["Nombre de répondants", "Taux d'emploi"])

with tab_nb:
    st.plotly_chart(fig_nb)
with tab_taux:
    st.plotly_chart(fig_taux)
    

st.markdown(
    """
    On remarque donc que ...
    """
)
