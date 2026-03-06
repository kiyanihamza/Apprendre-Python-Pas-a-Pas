# =================================================================
# EXPLICATION : elif = else if = sinon si.
# Python teste les conditions dans l'ordre et s'arrête dès qu'une est vraie.
#
# Ordre important : du plus strict au moins strict.
# Structure complète :
# if condition1:    → testé en premier
# elif condition2:  → si condition1 fausse
# else:             → si tout est faux
# =================================================================

note = 75

# TODO: Complète le barème de notation
if note >= 90:
    mention = 'Très bien'
elif __________: # Si la note est >= 70
    mention = 'Bien'
elif __________: # Si la note est >= 50
    mention = 'Passable'
else:
    mention = 'Insuffisant'

print(f'Note: {note}/100 — Mention: {mention}')
