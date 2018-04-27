"""
Use this class to create and write the
log file with the various events that
would occur within the application.
"""

import os

def _set_path():
    return os.path.join(os.getcwd(), 'Python\\Banque\\log_file.txt')

CURRENT_DIRECTORY = _set_path()

class LogFileHelper(object):
    def __init__(self, method_type, *kwargs):
        with open(CURRENT_DIRECTORY, method_type, encoding='utf-8') as f:
            f.writelines(kwargs)

LogFileHelper('w', 'Google', 'Facebook')