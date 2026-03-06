# =================================================================
# EXPLICATION : Une fonction c'est un bloc de code avec un nom.
# Règle DRY : Don't Repeat Yourself (ne te répète pas).
#
# Syntaxe :
# def nom_fonction(parametre):
#     instruction
#     return résultat
#
# La fonction ne s'exécute PAS quand tu la définis avec "def".
# Elle s'exécute seulement quand tu l'appelles.
# =================================================================

# TODO: Crée la fonction qui génère le message de bienvenue
def dire_bonjour(prenom):
    message = f'Bonjour {________} ! Bienvenue en Python.'
    return ________

# Appel de la fonction
resultat1 = dire_bonjour('Alice')
resultat2 = dire_bonjour('Bob')

print(resultat1)
print(resultat2)
print(dire_bonjour('Charlie'))
