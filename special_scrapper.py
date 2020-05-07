import os
import re
from io import TextIOWrapper
from urllib.parse import urljoin
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup
from matplotlib import image as pyimg
from PIL import Image

PATH = 'C:\\Users\\Pende\\Documents\\myapps\\my_python_codes\\test.html'

class Scrapper:
    def create_soup(self, handle=None):
        if handle and isinstance(handle, TextIOWrapper):
            return BeautifulSoup(handle, 'html.parser')

    def create_soup_from_file(self, path=None):
        with open(PATH, 'r', encoding='utf-8') as f:
            return self.create_soup(f)

class IOWriter:
    def to_folder(self, name):
        path = 'C:\\Users\\Pende\\Documents\\myapps\\my_python_codes'
        final_folder = os.path.join(path, name)
        os.mkdir(final_folder)
        with open(final_folder, 'w') as f:
            # with ZipFile(os.path.join(path, 'test.zip'), mode='w') as z:
            for link in 'links':
                response = requests.get(link)
                for content in response.iter_content(chunk_size=1024):
                    if content:
                        f.write(content)

class Query(Scrapper, IOWriter):
    def images(self, **attrs):
        s = 'Ashley in Fuel The Fire from Femjoy'
        images =  self.create_soup_from_file().find_all('img')
        # filtered_images = []
        for image in images:
            try:
                if image['alt'] == s:
                    link = image['src']
                    yield self.find_and_reconstruct_title(link)
            except KeyError:
                return []
    
    @staticmethod
    def find_and_reconstruct_title(link):
        is_match = re.search(r'(\w+\-)+\d+', link)
        if is_match:
            recreated_link = re.sub(r'(\w+\-).*', f'{is_match.group()}.jpg', link)
            return recreated_link
        return None


            
# query = Query()
# images = query.images()
# print(list(images)[:1])

# path = 'C:\\Users\\Pende\\Documents\\myapps\\my_python_codes\\test.jpg'
# image = Image.open(path)

# print(image)
