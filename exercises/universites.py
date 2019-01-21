#!/usr/bin/python

import os
import time
import subprocess
import sys
from subprocess import PIPE, call, check_output, Popen,STDOUT

CWD = os.getcwd()
DB_USER = os.environ.get('DB_USER')
DB_TABLE = os.environ.get('DB_TABLE')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def checker():
    script_path = os.path.join(CWD, 'my_python_codes', 'exercises')
    path_exists = os.path.exists(script_path)
    if path_exists:
        print('Script is correctly located')


def create_database():
    try:
        # Create the migrations
        return_code = call(['python', 'manage.py', 'makemigrations'], stderr=subprocess.STDOUT)
        return_code = call(['python', 'manage.py', 'migrate'], stderr=subprocess.STDOUT)
    except OSError as e:
        pass
    else:
        pass


def create_superuser(email, password):
    try:
        p = Popen(['python', 'manage.py', 'runserver'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    except OSError as e:
        pass
    else:
        p.communicate(input=b'pendenquejohn@gmail.com')
        time.sleep(1)
        p.communicate(input=b'touparet')
        time.sleep(1)
        status = p.communicate(input=b'touparet')
        print(status.decode())
        

# os.chmod(file_path, '777')
