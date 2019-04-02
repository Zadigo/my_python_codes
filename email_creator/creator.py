import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

NAMES_PATH = os.path.join(BASE_PATH, 'names.txt')

EMAILS_PATH = os.path.join(BASE_PATH, 'emails.txt')


def create(extension):
    with open(NAMES_PATH, 'r') as f:
        items = f.readlines()
        for item in items:
            lowered_name = item.lower().strip()
            name, sirname = lowered_name.split(' ')
            constructed_email = '%s.%s@%s' % (name, sirname, extension)
            items[items.index(item)] = constructed_email
        
        with open(EMAILS_PATH, 'a') as i:
            for item in items:
                i.writelines(item)
                i.writelines('\n')

create('adp.fr')
