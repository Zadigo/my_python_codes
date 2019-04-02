import os
import requests
import re
import time




BASE_PATH = os.path.dirname(os.path.abspath(__file__))

IMAGES_PATH = os.path.join(BASE_PATH, 'images')

# MAIN_IMAGES_PATH = os.environ.get('SpecialDownloads', IMAGES_PATH)

IMAGES_URLS = os.path.join(BASE_PATH, 'urls.txt')

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'



class Start:
    def __init__(self, file_name):
        print('Starting...')
        current_time = time.time()
        start_time = time.time()
        _iterator = self.last_number() or 0

        corrected_file_name = '_'.join(file_name.split(' '))
        partial_name = '%s_' % corrected_file_name

        with open(IMAGES_URLS, 'r') as u:
            urls = u.readlines()
            responses = self.get_responses(urls)

            for i in range(0, len(urls)):
                for response in responses:
                    if _iterator != 0 or _iterator is not None:
                        _iterator += 1
                        full_path_name = os.path.join(IMAGES_PATH, partial_name + str(_iterator) + '.jpg')
                    
                    else:
                        full_path_name = os.path.join(IMAGES_PATH, partial_name + str(i) + '.jpg')

                    if response.status_code == 200:
                        with open(full_path_name, 'wb') as f:
                            for chunk in response:
                                f.write(chunk)

        finish_time = time.time()
        completed_time = finish_time - current_time
        str_completed_time = '%s' % round(completed_time, 2)
        print('Finished:', str_completed_time)

    @staticmethod
    def get_responses(urls=[]):
        for url in urls:
            yield requests.get(url.strip(), USER_AGENT)

    def last_number(self):
        images = list(os.walk(IMAGES_PATH))[0][2]
        if images:
            last_image = images[-1]
            has_number = re.search(r'(\d+)\.', last_image)
            if has_number:
                return int(has_number.group(1))
        return None

Start('delilah belle hamlin')
