"""
https://developers.google.com/books/docs/v1/using#auth
"""

import urllib
import requests

# GOOGLE_BOOKS_SCOPE = 'https://www.googleapis.com/auth/books'
# GOOGLE_BOOKS_SCOPE = 'https://www.googleapis.com/books/v1/'

GOOGLE_BOOKS_URLS = [
    'https://www.googleapis.com/books/v1/volumes?'
]

GOOGLE_BOOKS_SECRET_KEY = 'AIzaSyBPeZd2aIwbdRR8mwdqJGlmGoEFIpatKoI'

class BaseGoogleBooks:
    fields = []
    query = {
        'q':'',
        'printType':'books',
        'key': GOOGLE_BOOKS_SECRET_KEY
    }
    search_book_url = 'https://www.googleapis.com/books/v1/volumes?'

    def _request(self, *args, **kwargs):
        if 'method' in kwargs:
            method = kwargs.get('method')
        if method == 'search':
            if 'author' in kwargs:
                author = kwargs.get('author')
            url = self.search_book_url + self._encode()
            url = url + '+' + author

        try:
            response = requests.get(url)
        except ConnectionError as error:
            print('There was an error %s' % error.args)
        else:
            if args:
                # Parse the args sent
                # by the user
                self.fields = args
                return self.parser(response.json())
            else:
                return response.json()

    def _encode(self):
        return urllib.parse.urlencode(self.query)

    def parser(self, obj):
        # TODO!!!!
        for field in self.fields:
            if field.startswith('items'):
                first_key, second_key = field.rsplit('_', 1)
                print(obj[first_key][0])

class BookSearch(BaseGoogleBooks):
    """
    Search the Google API for a given
    book providing a book name and an
    author.

    You can provide additional arguments
    such as the following in order to get
    specific items from the JSON file:
    > totalItems,
    > items,
    > items_volumeInfo,
    > items_volumeInfo_title,
    > items_volumeInfo_authors,
    > items_publisher,
    > items_publishedDate,
    > items_description,
    > items_industryIdentifiers,
    > items_language,
    > items_infoLink,
    > items_saleInfo,
    > items_retailPrice
    
    This is an example JSON return:
    https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes
    """
    def search_book(self, book_name, author, *args):
        # Google's book search url
        # includes an 'inauthor:'
        # field with which we need
        # deal. As the API key is
        # not an obligation, we can
        # pop it use the following
        # url : /?q=book+inauthor:author
        self.query.pop('key')
        self.query.update({'q':book_name})
        return self._request(
            *args,
            method='search',
            author='inauthor:' + author
        )

print(BookSearch().search_book('flowers', 'Keyes'))