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
df = pd.read_csv("stackoverflow_full.csv", index_col="Unnamed: 0")

# Ajout d'une colonne Code ISO (nécessaire pour les cartes)
iso = pd.read_excel("Liste-Excel-des-pays-du-monde.xlsx", skiprows=3)

iso_dict = iso.set_index('Nom anglais')['Code alpha-3'].to_dict()

dict_missing_values = {'United Kingdom of Great Britain and Northern Ireland' : 'GBR',
                       'Russian Federation' : 'RUS',
                       'United States of America' : 'USA',
                       'Netherlands' : 'NLD',
                       'Iran, Islamic Republic of...' : 'IRN',
                       'Hong Kong (S.A.R.)' : 'HKG',
                       'United Arab Emirates' : 'ARE',
                       'Bolivia' : 'BOL',
                       'Czech Republic' : 'CZE',
                       'The former Yugoslav Republic of Macedonia' : 'MKD',
                       'Venezuela, Bolivarian Republic of...' : 'VEN',
                       'Dominican Republic' : 'DOM',
                       'Syrian Arab Republic' : 'SYR',
                       'Taiwan' : 'TWN',
                       'South Korea' : 'KOR',
                       'Republic of Moldova' : 'MDA',
                       "Lao People's Democratic Republic" : 'LAO',
                       'Democratic Republic of the Congo' : 'COG',
                       'Philippines' : 'PHL',
                       'United Republic of Tanzania' : 'TZA',
                       'Kosovo' : 'XXK',
                       'Nomadic' : None,
                       'Congo, Republic of the...' : 'COG',
                       'Republic of Korea' : 'KOR',
                       'Swaziland' : 'SWZ',
                       'Libyan Arab Jamahiriya' : 'LBY',
                       'Sudan' : 'SDN',
                       'Palestine' : 'PSE',
                       'Cape Verde' : 'CPV',
                       'Niger' : 'NER',
                       'Gambia' : 'GMB'
                      }

iso_dict.update(dict_missing_values)

df['ISO'] = df['Country'].map(iso_dict)

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
