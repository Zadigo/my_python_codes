import os
import conf
from collections import OrderedDict
from utils import check_settings, folder_exists, has_pictures

class Engine:
    def __init__(self):
        attrs = check_settings()[0]
        for attr in attrs:
            if isinstance(attr, tuple):
                setattr(self, attr[0], attr[1])

        # Get default paths from dict
        self.default = self.IMAGES_PATHS['default']
        self.new_folder = self.IMAGES_PATHS['new_folder']

        # Check if both folders exist
        # Create if not the case
        folder_exists(self.default, self.new_folder)

class ImageEngine(Engine):
    def handle(self, new_name='image_'):
        images = os.listdir(self.default)

        if not images:
            raise TypeError('There were no images in %s' % 
            self.default)
        
        value_of_i = has_pictures(self.new_folder)
        # 
        if value_of_i:
            i = value_of_i
        else:
            i = 0

        for image in images:
            name, extension = str(image).rsplit('.', 1)
            if extension in self.IMAGES_TYPE:
                # Iterator for new image
                # name
                i += 1
                # Rename
                sortte = os.path.join(self.default, name), extension
                old_image = sortte[0] + '.' + sortte[1]
                constructed_new_path = os.path.join(self.new_folder, new_name + str(i) + '.' + sortte[1])
                os.rename(old_image,  constructed_new_path)


ImageEngine().handle()