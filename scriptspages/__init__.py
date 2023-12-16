# Script qui fait le lien entre les scripts individuels PAGE.py et la fonction principale de l'app (app.py)

# Ici on appelle les fonctions des pages dispos à partir des scripts de chaque page
# Syntaxe : from .NOMDELAPAGE import ST_NOMDELAPAGE

from .accueil import ST_ACCUEIL
from .graphe1 import ST_GRAPHE1
# from . graphe2 import ST_GRAPHE2

# On concatène les références de toutes les pages
ST_PAGES = {
    **ST_ACCUEIL,
    **ST_GRAPHE1,
#   ** ST_GRAPHE2 
}