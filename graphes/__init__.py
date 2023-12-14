# Script qui fait le lien entre les scripts individuels GRAPHE.py et la fonction principale de l'app (app.py)

# Ici on appelle les fonctions des graphes dispos
# A partir des scripts de chaque graphe
# Syntaxe : from .NOMDUGRAPHE import ST_NOMDUGRAPHE

from .graphe1 import ST_GRAPHE1
# from . graphe2 import ST_GRAPHE2

# On concatène les références de tous les graphes
ST_GRAPHES = {
    **ST_GRAPHE1,
#   ** ST_GRAPHE2 
}