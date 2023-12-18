# Taux d'emploi global

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

st.set_page_config(
    page_title="Taux d'emploi global", 
    page_icon=":chart_with_upwards_trend:"
)

st.markdown(
    """
    ## Taux d'emploi global

    """
)

# Chargement des données
df = pd.read_csv("stackoverflow_full.csv")

# Recodage des variables catégorielles (ENG -> FR)
df_fr = df.copy()

df_fr["EmployedCat"] = pd.cut(df_fr["Employed"], bins=[-1, 0, 1], labels=["Sans emploi", "En emploi"]).astype("object")

# 1. Graphe Age
fig = px.histogram(df_fr, x="EmployedCat", barmode="group", text_auto = True)

fig.update_layout(
    title_text="Distribution du statut d'emploi",
    xaxis_title_text="Statut d'emploi", 
    yaxis_title_text="Effectif",
    bargap=0.2, 
    bargroupgap=0.1 
)

st.plotly_chart(fig)

st.markdown(
    """
    On remarque donc que ...
    """
)
