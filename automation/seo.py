"""A module that regroups a list of SEO classes that
can serve to automate the checking of a website's content
"""

import re
from collections import Counter, deque
from itertools import dropwhile

import requests
from apscheduler.schedulers.blocking import BaseScheduler
from bs4 import BeautifulSoup

ARTICLES = {
    'fr': ('à', 'le', 'les', 'de', 'du', 'et')
}


class Errors:
    """A dictionnary that contains all the errors
    that were detected on a webpage
    """
    def __init__(self):
        base_errors = {
            'title': None,
            'description': None,
            'images': None
        }
        self.base_errors = self._init_errors(base_errors)

    @staticmethod
    def _init_errors(items:dict):
        for key in items.keys():
            items[key] = deque()
        return items

    def append(self, error_name, value):
        if error_name in self.base_errors:
            self.base_errors[error_name].append(value)
        return self.base_errors[error_name]

    @property
    def show_errors(self):
        return self.base_errors

class Analyzer:
    content = None

    def length(self, content):
        return content.length()

    def words(self):
        return self.content.split(' ')

    def word_count(self):
        return len(self.words())

    @classmethod
    def as_class(cls, content):
        klass = cls()
        klass.content = content
        return klass

class SEO:
    analyzer = Analyzer
    errors = Errors()

    def create_request(self, url, **extra_headers):
        self.url = url
        self.extra_headers = extra_headers
        self.soup = None

        headers = {}
        response = requests.get(url, headers={**headers, **extra_headers})
        
        return BeautifulSoup(response.text, 'html.parser') \
                if response.status_code == 200 else None

    @staticmethod
    def check_soup(soup):
        return soup if soup else None

class Title(SEO):
    """Get the title of a given document"""
    def __init__(self, url):
        document = super().create_request(url)
        if document:
            title_text = document.find('title').text
            self.title = title_text or None
            self.analyzis = self.analyzer.as_class(self.title)

    # def clean_title(self, lang='fr'):
    #     """A definition that eliminates the articles from the title"""
    #     def drop(word): word if word not in ARTICLES[lang] else None
    #     return dropwhile(drop, self.analyzis.words())

class Keywords(SEO):
    def __init__(self, url):
        document = self.check_soup(super().create_request(url))
        keywords_tags = document.find_all('meta', attrs={'name': 'keywords'})
        if keywords_tags:
            self.keywords = (keywords_tag['content'] for keywords_tag in keywords_tags)
        else:
            print('There are no keywords no this website')

class Description(SEO):
    """Analyze the description of a website"""
    def __init__(self, url):
        document = self.check_soup(super().create_request(url))
        # Find all the tags present on the website --;
        # we should normally only get one tag.
        description_tags = document.find_all('meta', attrs={'name': 'description'})

        # A website should only have one description
        # tag. If there are many, then something is
        # not right
        has_many_tags = len(description_tags) > 0
        if has_many_tags:
            self.errors.append('description', [description_tag['content'] for description_tag in description_tags if description_tag])
        
        description_tag = description_tags[0]

        self.description = description_tag['content']
        self.analyzis = self.analyzer.as_class(self.description)

    @property
    def description_text(self):
        """Return the text within the description tag"""
        return self.description

    def __str__(self):
        return f'{self.__class__.__name__}(content="{self.description_text}")'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.description_text)

class Images(SEO):
    """Analyzes each image and checks if they have an `src`
    and `alt` attributes
    """
    def __init__(self, url):
        document = self.check_soup(super().create_request(url))
        website_images = document.find_all('img')
        for website_image in website_images:
            if 'alt' not in website_image:
                self.errors.append('images', website_image['src'])



# title = Title('https://www.dorchestercollection.com/fr/paris/le-meurice/spa/soins/')
# print(list(title.clean_title()))

# images = Images('https://www.dorchestercollection.com/fr/paris/le-meurice/spa/soins/')
# print(images.errors.show_errors)


# a = Analyzer()
# b = a.as_class('This is content')
# print(b.words())
