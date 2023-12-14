# Script pour générer le graphe 1

## A noter : aussi possible de regrouper plusieurs graphes entre eux. Par exemple si ils ont la même forme ou considèrent le même genre de données / les mêmes variables
## Dans ce cas : définir leurs fonctions les unes après les autres : graphe 1(), graphe2()
## Dans le ST_GRAPHE : mettre plusieurs entrées. 
## Syntaxe : ST_GROUPE1 = {"Groupe 1 : Graphe 1": graphe1, "Groupe 1 : Graphe 2": graphe2}
## Ensuite on aura bien toutes les entrées du ST_GROUPE1 dans le ST_GRAPHES concaténé (__init__.py)

import streamlit as st

# Fonction qui permet de générer le graphe souhaité : 
def graphe1():
    b = (
        Bar()
        .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
        .add_yaxis("2017-2018 Revenue in (billion $)", random.sample(range(100), 10))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
            ),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    st_pyecharts(
        b, key="echarts"
    )  # Add key argument to not remount component at every Streamlit run

# ST_GRAPHE1 est un dictionnaire où l'on a le nom du graphe et le nom de sa fonction
# Sert pour ensuite être intégré à la liste des graphes dispos et être appelé dans app.py
ST_GRAPHE1 = {"Graphe 1": graphe1}