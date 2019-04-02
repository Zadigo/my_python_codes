from itertools import permutations
import csv
import os


PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(PATH, 'emails.txt')

def create_csv(func):
    def _create(nom, prenom):
        with open(CSV_PATH, 'w') as f:
            for email in func(nom, prenom):
                f.writelines(email)
                f.writelines('\n')
    return _create

@create_csv
def gmail(nom, prenom):
    emails = [f'{nom}.{prenom}', f'{prenom}.{nom}', f'{nom}-{prenom}',
        f'{prenom}-{nom}', f'{nom}_{prenom}', f'{prenom}_{nom}', f'{prenom}{nom}',
        f'{nom}{prenom}', f'{nom[:1]}{prenom}', f'{prenom[:1]}{nom}']

    for email in emails:
        index = emails.index(email)
        email = email + '@gmail.com'
        emails[index] = email

    return emails

gmail('antoine', 'hucher')