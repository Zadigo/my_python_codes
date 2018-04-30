"""
This module receives a response, which can
be the instance of a class in order to
parse the HTML page in with Beautifulsoup.
"""

import collections
from bs4 import BeautifulSoup
from responses import BaseResponse

BEAUTY = collections.namedtuple('HTML', ['text'])

class BeautifulResponse(BaseResponse):
    responses = None
    html_tags = None
    instance = BaseResponse()

    @staticmethod
    def _soup_factory(html_tags):
        return BeautifulSoup(html_tags.text, 'html.parser')

    def beautify_response(self, Klass=None):
        # We have to be able to get an instance
        # wether we call method from class
        # or if we superclass
        if  Klass is None:
            Klass = self.instance

        # We need to set attributes of the
        # empty instance method otherwise
        # they would be none
        Klass.__setattr__('urls', self.urls)
        Klass.__setattr__('useragent', self.useragent)
        
        self.responses = Klass.get_response()

        # Get the html text elements from
        # each response and return a list
        self.html_tags = [self._soup_factory(response) for response in self.responses if response is not None]

class ExtractImages(BeautifulResponse):
    """
    This extracts all images from the html tags
    """
    def get_images(self):
        super().beautify_response()
        return self.html_tags[0].findAll('img')

class ExtractLinks(BeautifulResponse):
    """
    This extracts all images from the html tags
    """
    def get_images(self):
        super().beautify_response()
        return self.html_tags[0].findAll('a')
