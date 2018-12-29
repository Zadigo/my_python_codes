import random
import itertools
from collections import namedtuple

noms = ['Pauline', 'Mathieu', 'Constance', 'Emilie']
matieres = ['Marketing', 'Finance', 'Mathematique']

def create_scores():
    eleves = []
    for nom in noms:
        eleve = {
            'nom': nom
        }
        for matiere in matieres:
            eleve.update({matiere: random.randrange(0, 20)})

        eleves.append(eleve)

    return eleves

def create_data(eleves=create_scores()):
    s = namedtuple('Etudiant', ['nom', 'moyenne'])
    for eleve in eleves:
        total = 0
        for key, value in eleve.items():
            if key == 'nom':
                nom = value

            else:
                total += value

        yield s(nom, round(total / 3, 1))

# passage = itertools.takewhile(lambda x: x[1] >= 10, create_data())

# print(list(passage))


letters = ['A', 'B', 'C', 'D', 'E']

def create_combination():
    combined = itertools.combinations(letters, 2)
    random.shuffle(list(combined))

create_combination()
