import datetime

def get_age(date_of_birth):
    year_of_birth = datetime.datetime.timetuple(datetime.datetime.strptime(date_of_birth, '%d/%m/%Y'))[0]
    return datetime.datetime.now().year - year_of_birth
    