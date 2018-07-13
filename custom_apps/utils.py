import re
import random
import string
from urllib.parse import urlencode
from datetime import timedelta
import datetime

from django.utils.text import slugify

class SlugGenerator:
    @classmethod
    def random_string_generator(self, size=10, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def unique_slug_generator(self, instance, new_slug=None):
        if  new_slug is not None:
            slug = new_slug
        else:
            slug = slugify(instance.title)

        Klass = instance.__class__
        qs_exists = Klass.objects.filter(slug=slug).exists()
        if qs_exists:
            new_slug = '{slug}-{randstr}'.format(
                slug=slug,
                randstr=self.random_string_generator(size=4)
            )
            return self.unique_slug_generator(instance, new_slug=new_slug)
        return slug

def lowercase_names(*args):
    if  not args:
        return []

    postes = []
    new_poste = ''
    for arg in args:
        words = str(arg).split(' ')

        for word in words:
            new_poste += word.lower() + '-'
            new_poste_slug = re.search(r'([a-z\-]+)(\-)', new_poste).group(1)
        postes.append(new_poste_slug)
        new_poste = ''
    return postes

def lowercase_slug_name(nom_poste):
    words = str(nom_poste).split(' ')
    word = '-'.join(words)
    return word.lower()

def unslug_nom_poste(nom_poste, capitalize=False):
    words = str(nom_poste).split('-')
    word = ' '.join(words)
    if  capitalize is True:
        word = str(word).capitalize()
    return word

# Context

class ContextBuilder:
    context = {}
    def __init__(self, request=None, *args, **kwargs):
        if args:
            for arg in args:
                self.context[arg] = arg

        if kwargs:
            for key, value in kwargs.items():
                self.context[key] = value

    @property
    def get_context(self):
        return self.context or {}

# models.py

# slug = models.SlugField(max_length=50)
# def save(self, *args, **kwargs):
#     if not self.id:
#         self.slug = slugify(unidecode(self.nom_poste))

#     super(test, self).save(*args, **kwargs)

# def create_param_link(base_url='', **kwargs):
#     q = dict()
#     def _iterator(urls, param):
#         if isinstance(urls, dict) or isinstance(urls, str):
#             raise TypeError('There was an error. Receive %s' % urls)
#         return [url for url in urls]

#     def test_url(url):
#         pattern = r'https?\:\/\/www\.\w+\.\w+'
#         base_url_correct = re.match(pattern, base_url)
#         if base_url_correct is None:
#             raise TypeError('Did you check your url? %s' % base_url)
# # 
#     if kwargs:
#         for key, value in kwargs.items():
#             q[key] = value
#     params = '?' + urlencode(q, encoding='utf-8')
#     if base_url:
#         test_url(base_url)
#         # _iterator(test_url(base_url), params)
        
        

#     return base_url + params or params

# print(create_param_link(base_url='http://www.goog.io/', a='a', b='b'))

def date_calculator(method='add', date1=datetime.datetime.now(), days=1):
    """
    Returns the current date plus x amount of
    days if nothing was specified or, the user
    specified date plus x amount of days
    """
    if isinstance(date1, str):
        p = datetime.datetime.strptime(date1, "%m-%d-%Y")
    else:
        p = date1
    
    if method == 'add':
        r = p + timedelta(days=days)
    elif method == 'substract':
        r = p - timedelta(days=days)
    else:
        raise TypeError('Did you mean \'add\' or \'substract\'?')
    return r


class A:
    def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
        self = object.__new__(cls)
        self._hour = hour
        print(cls)
        return self

    @property
    def hour(self):
        return self._hour