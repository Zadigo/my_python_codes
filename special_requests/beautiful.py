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
    response = None
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

        # If instance is a method
        if not isinstance(Klass, BaseResponse):
            is_callable = callable(Klass)
            if is_callable:
                # We have to pass response in a list
                # for now otherwise we get a byte response
                # since Beautiful soup is looking for a list
                # to iterate over
                self.response = [Klass()]
                
                if self.response:
                    pass
                else:
                    raise TypeError('Response is None.')

            else:
                raise TypeError('You should pass a function or an instance. Received %s' % Klass)

        else:
            # We need to set attributes of the
            # empty instance method otherwise
            # they would be none
            Klass.__setattr__('urls', self.urls)
            Klass.__setattr__('useragent', self.useragent)
            self.response = Klass.get_response()

        if self.response:
            # Keep only responses that received a
            # status_code of 200
            sorted_response = [response for response in self.response if response.status_code == 200]
            
            if len(sorted_response) == 0:
                return []
        else:
            return []

        # Get the html text elements from
        # each response and return a list
        self.html_tags = [self._soup_factory(single_response) for single_response in sorted_response]

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