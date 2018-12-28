import datetime
import time

class Prisme:
    def __init__(self, salaire, date_debut, date_fin, **kwargs):
        salaire_moyen = 1500
        ratio = round(salaire / salaire_moyen, 2)

        if salaire < 1000:
            pass

        elif salaire >= 1000 and salaire < 1500:
            pass

        else:
            pass

        date_debut = datetime.datetime.strptime(date_debut, '%Y-%m-%d')
        date_fin = datetime.datetime.strptime(date_fin, '%Y-%m-%d')
        ecart = date_debut - date_fin

        if ecart.days < 0:
            pass

        liste_des_salaires = []

        for i in range(0, abs(ecart.days)):
            if i == 0:
                salaire_augmente = salaire

            salaire_augmente = salaire_augmente * 1.005
            liste_des_salaires.append((i, round(salaire_augmente, 2)))

        i = 0
        self.salaires_moins_impot = list(map(lambda x: (i, x[1] / 1.4), liste_des_salaires))

    @property
    def get_salaires_moins_impot(self):
        return self.salaires_moins_impot

    @classmethod
    def _aides_sociales(cls):
        s = cls(1785, '2018-12-1', '2018-12-5').get_salaires_moins_impot
        c = cls(1478, '2018-12-1', '2018-12-5').get_salaires_moins_impot
        print(s,c)

p=Prisme(1575,'2018-12-1','2018-12-5')
print(p.get_salaires_moins_impot)
p._aides_sociales()
