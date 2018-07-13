import os
import re
# from subprocess import call

__version__ = '0.0.1'

def _create_path():
    userprofile = os.getenv('USERPROFILE', default=None)
    path = os.path.join(userprofile, 'Downloads')
    return path

PATH = _create_path()

def _walk_path(path, arg=None):
    if  arg is None:
        # Show everything
        for root, dirs, files in os.walk(path):
            print(root)
    else:
        # Show a speciic ie
        for root, dirs, files in os.walk(path):
            if os.path.basename(root) == arg:
                print(root)

# _walk_path(PATH, arg='fonts2')

# call("echo Hello World", shell=True)

with open('test.bat', 'w', encoding='utf_8') as t:
    t.writelines('%')
    t.writelines('ECHO OFF')
    t.writelines('\n')
    