import os
import re
import sys
import time
import zipfile
import subprocess as sb
# from subprocess import call

PATH = os.getenv('USERPROFILE', default=None)

if PATH is None:
    pass

R_PATH = os.path.join(PATH, 'Downloads')
N_PATH = os.path.join(R_PATH, 'onts2')

try:
    t_files = os.listdir(R_PATH)
    # if zp.is_zipfile(R_PATH) is False:
    #     pass
    # else:
    #     print('t')
    # fonts = os.listdir(R_PATH)
except FileExistsError as e:
    print(e.args)

for t_file in t_files:
    if t_file == 'fonts2.zip':
        a = os.path.join(R_PATH, t_file)
        break

zt = zipfile.ZipFile(a, mode='r')
zt.extractall(path=N_PATH)


# for font in fonts:
    # time.sleep(3)
    # binary_path = os.path.join(R_PATH, font)
    # sb.call(binary_path)
    # os.execl(binary_path, *sys.argv)
    # call('echo {}'.format(font))
    # time.sleep(2)