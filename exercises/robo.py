import re
import time
import json
from robobrowser import RoboBrowser


JSON_FILE = 'D:\\Programs\\Repositories\\my_python_codes\\exercises\\emails.json'

def robo_questor():
    url = 'http://franckcrepelle.com/fix_mail.php'

    browser = RoboBrowser(history=True)
    browser.open(url, method='get')

    f = open(JSON_FILE, 'r', encoding='utf-8')
    emails = json.load(f)['emails']

    contact_form = browser.get_form(id=re.compile(r'frm[0-9]+'))
    for email in emails:
        print('Sending for %s' % email)
        contact_form['contact_name'].value = email
        contact_form['contact_email'].value = email
        contact_form['contact_msg'].value = f"""
        Bonjour,

        Je souhaiterai connaître vos tarifs pour un travail
        de peinture à sur un domicile de 785m2.

        Contactez-moi à l'adresse qui suit {email}.

        Cordialement.
        """

        browser.submit_form(contact_form)

    f.close()

robo_questor()
