'''
Something
'''
import os
import re

# path = f'D:/HTML/Programs/Python/image_handling/images/'
IMAGES_PATH = 'D:\\Programs\\Python\\images'

PATTERNS = [
    r'([Kk]imberl(y|ey))(\-|_)([Gg]arner)'
]

def _new_folder_path_exists():
    new_images_folder = os.path.join(IMAGES_PATH, 'Kimberley Garner')
    if not os.path.exists(new_images_folder):
        os.mkdir(new_images_folder)
    return new_images_folder

# _new_folder_path_exists()

def change_names():
    '''
    Something
    '''

    images_list = os.listdir(IMAGES_PATH)

    splitted_images = [str(image).split('.') for image in images_list]

    filtered_images = [splitted_image for splitted_image in splitted_images if re.search(PATTERNS[0], str(splitted_image))]
    filtered_images_path = [os.path.join(IMAGES_PATH, filtered_image[0] + '.' + filtered_image[1]) for filtered_image in filtered_images]
    
    new_folder_for_images_path = _new_folder_path_exists()

    for i in range(0, len(filtered_images_path)):
        new_image_path = os.path.join(new_folder_for_images_path, 'Kimberly-Garner_{0}.{1}'.format(i, filtered_images[0][1]))
        os.rename(filtered_images_path[i], new_image_path)

change_names()
