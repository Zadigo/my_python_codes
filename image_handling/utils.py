import conf
import os
import re
from collections import namedtuple

def check_settings():
    attrs = dir(conf)

    check = (
        'IMAGES_PATH',
        'IMAGES_TYPE',
    )

    attributes = []
    
    settings = namedtuple('SETTINGS', ['values'])
    for attr in attrs:
        if attr.upper() and attr in check:
            value = getattr(conf, attr)
            # Should be list or tuple
            if not isinstance(value, (list, tuple, dict)):
                raise TypeError('%s is not a tuple or a list', (
                    attr, 
                ))

        if attr.isupper():
            attributes.append((attr, getattr(conf, attr)))

    if len(attributes) == 0:
        raise AttributeError('Could not find BASE_DIR, '
        'IMAGES_PATH, IMAGES_TYPE attributes in conf')
    
    return settings(attributes)

def folder_exists(*folder_paths):
    """
    Checks whether a folder
    exists in the application scope
    """
    for folder_path in folder_paths:
        exists = os.path.exists(folder_path)

        if not exists:
            print('Creating folder: %s' % folder_path)
            os.mkdir(folder_path)

def regex_helper():
    pass

def has_pictures(folder_path):
    images = os.listdir(folder_path)
    # if images:
    #     name_format = re.search(r'image\_(\d+)', images[-1])
    #     if name_format:
    #         # Return the last images number
    #         # and iterating from there
    #         print(int(name_format.group(1)))
    #         return int(name_format.group(1))
    #     else:
    #         return False
    # else:
    #     return False

has_pictures(conf.IMAGES_PATHS['new_folder'])




# import os
# import re

# # path = f'D:/HTML/Programs/Python/image_handling/images/'
# IMAGES_PATH = 'D:\\Programs\\Python\\images'

# PATTERNS = [
#     r'([Kk]imberl(y|ey))(\-|_)([Gg]arner)'
# ]

# def _new_folder_path_exists():
#     new_images_folder = os.path.join(IMAGES_PATH, 'Kimberley Garner')
#     if not os.path.exists(new_images_folder):
#         os.mkdir(new_images_folder)
#     return new_images_folder

# # _new_folder_path_exists()

# def change_names():
#     '''
#     Something
#     '''

#     images_list = os.listdir(IMAGES_PATH)

#     splitted_images = [str(image).split('.') for image in images_list]

#     filtered_images = [splitted_image for splitted_image in splitted_images if re.search(PATTERNS[0], str(splitted_image))]
#     filtered_images_path = [os.path.join(IMAGES_PATH, filtered_image[0] + '.' + filtered_image[1]) for filtered_image in filtered_images]
    
#     new_folder_for_images_path = _new_folder_path_exists()

#     for i in range(0, len(filtered_images_path)):
#         new_image_path = os.path.join(new_folder_for_images_path, 'Kimberly-Garner_{0}.{1}'.format(i, filtered_images[0][1]))
#         os.rename(filtered_images_path[i], new_image_path)

# change_names()
