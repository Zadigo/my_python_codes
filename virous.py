import os
# import re

# PATTERN = r'\.(txt|xslx|xls|pptx|doc|docx|pdf|csv|rtf)'

# BASE_PATH = os.path.abspath(__file__)

# USERPROFILE = os.getenv('USERPROFILE')
# TEMP = os.getenv('TMP')
# BUREAU = os.path.join(USERPROFILE, 'Desktop')
# DOCS = os.path.join(USERPROFILE, 'Documents')

# def search(path):
#     all_files = []
#     folders = os.walk(path)
#     for folder in folders:
#         for file in folder:
#             if isinstance(file, list):
#                 for element in file:
#                     result = re.search(PATTERN, element)
#                     if result:
#                         true_path = os.path.join(folder[0], element)
#                         all_files.append(true_path)
#     return all_files or None

# def _delete(files):
#     debug = False
#     error_files = []

#     if debug is False:
#         try:
#             for file in files:
#                 # result = os.remove(file)
#                 print('delete', file)
#         except NotImplementedError:
#             error_files.append(file)
        
#         # if result is None:
#         #     error_files.append(file)
                
#     return error_files or True

# mydocuments = search(DOCS)
# myhome = search(BUREAU)
# _delete(mydocuments)

os.mkdir('C:\\Users\\Pende\\Documents\\test')