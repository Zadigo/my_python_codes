import configuration
import os

files = list(os.walk(configuration.BASE_DIR))
for _file in files:
    if isinstance(_file, tuple):
        for element in _file:
            if isinstance(element, list) and len(element) > 2:
                if 'base.py' in element:
                    element.remove('.gitignore')
