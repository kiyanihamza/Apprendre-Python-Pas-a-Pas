# =================================================================
# EXPLICATION : if/else c'est exactement comme dans la vraie vie :
# SI (if) une condition est vraie → fais ça
# SINON (else) → fais autre chose
#
# Syntaxe :
# if condition:
#     instruction  <-- 4 espaces obligatoires !
# else:
#     instruction  <-- 4 espaces obligatoires !
#
# Les opérateurs de comparaison :
# >= (supérieur ou égal), <= (inférieur ou égal), == (égal), != (différent)
#
# ⚠️ ERREUR CLASSIQUE : oublier les 4 espaces (indentation)
# =================================================================

age = 17

# TODO: Complète la condition pour vérifier si l'âge est suffisant pour voter (18 ans)
if __________:
    print('Tu es majeur, tu peux voter')
else:
    print(f'Tu es mineur, encore {18 - age} ans a attendre')
