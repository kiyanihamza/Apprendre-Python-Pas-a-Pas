# =================================================================
# EXPLICATION : Calcule la somme de 1 à 100 avec une boucle.
# Ce que le mathématicien Gauss faisait à la main, Python le fait 
# instantanément.
#
# La technique : L'accumulateur
# somme = 0      --> on commence à zéro
# somme += n     --> on ajoute la valeur de n à chaque tour
#
# Tour par tour :
# n=1 : somme = 0 + 1 = 1
# n=2 : somme = 1 + 2 = 3
# ...
# n=100 : somme = ... + 100 = 5050
#
# 💡 ASTUCE : somme += n est un raccourci pour somme = somme + n
# range(1, 101) permet d'aller de 1 jusqu'à 100 (le 101 est exclu).
# =================================================================

# On initialise la variable à 0
somme = 0

# TODO: Crée une boucle qui parcourt les nombres de 1 à 100
for n in range(1, ________):
    # TODO: Ajoute n à la variable 'somme' à chaque tour (utilise +=)
    somme __________ n

# Affichage du résultat final
print(f'Somme de 1 à 100 = {somme}')

# Le résultat attendu est : 5050
