# Variables catégorielles : mosaïques

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Variables catégorielles : mosaïques", 
    page_icon=":chart_with_upwards_trend:"
)

st.markdown(
    """
    ## Variables catégorielles : mosaïques

    Les mosaïques ci-dessous décrivent le lien entre statut d'emploi et les quatre variables catégorielles principales : l'âge, le genre, le niveau d'éducation et la branche principale.
    """
)

df = pd.read_csv("stackoverflow_full.csv")

# Âge vs. Employé
mosaic(df, index=["Employed","Age"])
plt.title("Distribution de l'âge vs. Statut d'emploi")
st.pyplot()

# Genre vs. Employé
mosaic(df, index=["Employed","Gender"])
plt.title('Distribution du genre vs. Statut d\'emploi')
st.pyplot()

# Niveau d'éducation (EdLevel) vs. Employé
mosaic(df, index=["Employed","EdLevel"])
plt.title('Niveau d\'éducation vs. Statut d\'emploi')
st.pyplot()

# Branche principale (MainBranch) vs. Employé
mosaic(df, index=["Employed","MainBranch"])
plt.title('Branche principale vs. Statut d\'emploi')
st.pyplot()
