import random

grille = [n for n in range(1, 51)]
stars = [n for n in range(1, 13)]

def start():
    grille_play = sorted(random.choices(grille, k=5))
    stars_play = sorted(random.choices(stars, k=2))

    return grille_play, stars_play

print(start())
