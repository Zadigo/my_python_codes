import datetime

def get_age(year_of_birth):
    return datetime.datetime.now().year - year_of_birth
