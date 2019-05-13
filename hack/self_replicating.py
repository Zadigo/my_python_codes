# import os
# from sys import argv
# from win32com import client

# # D:\Programs\Python
# CURRENT_PATH = os.system('cd')
# # desktop_path = os.getenv('USERPROFILE')
# program_files = os.getenv('PROGRAMFILES')

# def make_directories():
#     # directories = ['a', 'b', 'c', 'e']
#     # for directory in directories:
#     #     try:
#     #         os.mkdir('clone')
#     #         current_dir = os.path.join(CURRENT_PATH, 'text.txt')
#     #         new_dir = os.path.join(directory, 'text.txt')
#     #         os.rename(current_dir, new_dir)
#     #     except FileExistsError:
#     #         pass

#     os.mkdir('clone')
#     os.rename('D:\\Programs\\Python\\python_codes\\test.txt', 'D:\\programs\\Python\\python_codes\\clone\\test.txt')

# def create_shortcut_icon():
#     path = os.path.join(str(CURRENT_PATH), 'Internet Explorer.lnk')
#     target = r'D:\\Programs\\Python\\python_codes\\clone'
#     working_directory = r'D:\\Programs\\Python\\python_codes'
#     icon_location = r'C:\\Program Files (x86)\\Internet Explorer\\iexplorer.exe'

#     shell = client.Dispatch('Wscript.Shell')
#     shortcut = shell.CreateShortCut(path)
#     shortcut.Targetpatch = target
#     shortcut.WorkingDirectory = working_directory
#     shortcut.IconLocation = icon_location
#     shortcut.save()

# make_directories()
# # create_shortcut_icon()

# # def cloner(test=True):
# #     script = argv 
# #     name = str(script[0])
# #     os.system('start test.txt')
# #     os.mkdir('clone')
# #     os.system(r'copy test.txt clone')
# #     # os.system(r'copy ' + name + ' clone')

# # cloner()


import pathlib
import os
import configparser

BASE_PATH = os.path.abspath(__file__)

def make_directories():
    dirs_to_create = ['a', 'b', 'c']
    for dir_to_create in dirs_to_create:
        dirs_to_create[dirs_to_create.index(dir_to_create)] = \
            os.path.join(BASE_PATH, dir_to_create)

    dir_exists = 

    print(dirs_to_create)

make_directories()
