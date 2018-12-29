import subprocess
from dataclasses import dataclass

args=['%s']
cmdline = ['name'] + [arg.replace("%s", 'url')
                                 for arg in args]

print(cmdline)