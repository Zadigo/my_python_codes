"""
This creates an html oer ie with a
ht page, a uery in an
"""

import os
import json

ENV_PATH = os.getenv('USERPROFILE', default=None)
PATH = os.path.join(ENV_PATH, 'Downloads', 'testing')

html_file_path = os.path.join(PATH, 'test' + '.' + 'html')
css_file_path = os.path.join(PATH, 'test' + '.' + 'css')
js_file_path = os.path.join(PATH, 'test' + '.' + 'js')

def _the_path_exists():
    return os.path.exists(PATH)

def _directory_helper():
    if _the_path_exists() is True:
        pass
    else:
        try:
            os.makedirs(PATH)
        except FileExistsError as error:
            print(error.args)

def _write_files(bootstrap=True):
    if bootstrap is False:
        pass
    else:
        # Open the json
        with open('content.json', 'r', encoding='utf_8') as json_file:
            tags = json.load(json_file)
            # Open or create the files
            with open(html_file_path, 'w', encoding='utf_8') as html_file:
                for tag in tags['html']['content']:
                   html_file.writelines(tag)
            with open(css_file_path, 'w', encoding='utf_8') as html_file:
                for tag in tags['css']['content']:
                   html_file.writelines(tag)
            with open(js_file_path, 'w', encoding='utf_8') as html_file:
                for tag in tags['jquery']['content']:
                   html_file.writelines(tag)

def Main():
    _directory_helper()
    _write_files()

if __name__ == '__main__':
    Main()