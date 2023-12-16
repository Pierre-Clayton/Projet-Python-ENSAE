# Graphe 1

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic
from wordcloud import WordCloud

st.set_page_config(
    page_title="Graphe 1", 
    page_icon=":chart_with_upwards_trend:"
)


st.markdown(
    """
    ## Graphe 1
    """
)

df = pd.read_csv("stackoverflow_full.csv")
