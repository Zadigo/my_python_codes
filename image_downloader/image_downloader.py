import os
import requests
import re
import time
import datetime
import secrets
import argparse

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

IMAGES_PATH = os.path.join(os.environ.get('USERPROFILE'), 'Downloads')

DOWNLOAD_DIRS = {
    'default': os.path.join(IMAGES_PATH, 'www_downloads'),
    'others': []
}

class DownloadImage:
    def __init__(self, url):
        # Check if directories exists
        # and create them if necessary
        default_dir = DOWNLOAD_DIRS['default']
        if not os.path.exists(default_dir):
            try:
                print(f'Creating dowload folder to: {default_dir}')
                os.mkdir(default_dir)
            except os.error:
                raise

        # Parameters to create a
        # subdirectory in the dowload folder
        # current_date = datetime.datetime.now().date()
        # sub_directory_name = '%s_%s_%s_%s' % (
        #     current_date.day(),
        #     current_date.month(),
        #     current_date.year(),
        #     secrets.token_hex(5)
        # )
        # sub_directory_path = os.path.join(default_dir, sub_directory_name)
        # os.mkdir(sub_directory_path)
        # os.chdir(sub_directory_path)

        response = self.create_request(url)
        self.write_image(response, to_path=default_dir)


    @staticmethod
    def create_request(url):
        try:
            response = requests.get(url)
        except requests.HTTPError:
            raise
        else:
            if response.status_code == 200:
                return response
            return None

    @staticmethod
    def write_image(response, **kwargs):
        print('Writing images...')
        with open(kwargs['to_path'], 'wb') as f:
            for chunk in response:
                f.write(chunk)


# DownloadImage('https://www.sawfirst.com/wp-content/uploads/2019/05/Romee-Strijd-at-The-Dead-Dont-Die-Opening-Ceremony-19.jpg')








# IMAGES_PATH = os.path.join(BASE_PATH, 'images')

# # MAIN_IMAGES_PATH = os.environ.get('SpecialDownloads', IMAGES_PATH)

# IMAGES_URLS = os.path.join(BASE_PATH, 'urls.txt')

# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
#                 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'



# class Start:
#     def __init__(self, file_name):
#         print('Starting...')
#         current_time = time.time()
#         start_time = time.time()
#         _iterator = self.last_number() or 0

#         corrected_file_name = '_'.join(file_name.split(' '))
#         partial_name = '%s_' % corrected_file_name

#         with open(IMAGES_URLS, 'r') as u:
#             urls = u.readlines()
#             responses = self.get_responses(urls)

#             for i in range(0, len(urls)):
#                 for response in responses:
#                     if _iterator != 0 or _iterator is not None:
#                         _iterator += 1
#                         full_path_name = os.path.join(IMAGES_PATH, partial_name + str(_iterator) + '.jpg')
                    
#                     else:
#                         full_path_name = os.path.join(IMAGES_PATH, partial_name + str(i) + '.jpg')

#                     if response.status_code == 200:
#                         with open(full_path_name, 'wb') as f:
#                             for chunk in response:
#                                 f.write(chunk)

#         finish_time = time.time()
#         completed_time = finish_time - current_time
#         str_completed_time = '%s' % round(completed_time, 2)
#         print('Finished:', str_completed_time)

#     @staticmethod
#     def get_responses(urls=[]):
#         for url in urls:
#             yield requests.get(url.strip(), USER_AGENT)

#     def last_number(self):
#         images = list(os.walk(IMAGES_PATH))[0][2]
#         if images:
#             last_image = images[-1]
#             has_number = re.search(r'(\d+)\.', last_image)
#             if has_number:
#                 return int(has_number.group(1))
#         return None

# Start('delilah belle hamlin')

def Main():
    args = argparse.ArgumentParser(description='Download an image from a url')
    args.add_argument('url', help='Enter a url of the image to download', type=str)
    args.add_argument('-p', '--path', help='Path to dowload images to')
    args.add_argument('-r', '--rename', help='Save file with a specific name', type=str)
    parsed_args = args.parse_args()

    if args:
        print(parsed_args.path)

if __name__ == "__main__":
    Main()

# r'[a-zA-Z]?\:?\\\\(\w+\\)\?'
# r'(\/\w+)+'
# r'(https?\:\/\/\)?(www\.)?\w.*(\.\w+)'