import collections
from bs4 import BeautifulSoup
from .responses import BaseResponse

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

        else:
            self.instance = Klass

        if Klass is None or self.instance is None:
            raise TypeError('Not an instance. Receive none')

        if not isinstance(Klass, BaseResponse):
            raise TypeError('Not an instance of BaseResponse. Receive %s' % Klass.__class__.__name__)

        assert isinstance(Klass, BaseResponse) is True
        assert Klass is not None
        # We need to set attributes of the
        # empty instance method otherwise
        # they are none
        Klass.__setattr__('urls', self.urls)
        Klass.__setattr__('useragent', self.useragent)
        
        # Get requests
        self.responses = Klass.get_response()
        # assert self.responses is None

        # Get the html text elements from
        # each response and return a list
        self.html_tags = [self._soup_factory(response) for response in self.responses if response is not None]
        # assert self.html_tags is None



# class ExtractImages(BeautifulResponse):
#     """
#     This extracts all images from the html tags
#     """
#     def get_images(self, *args):
#         self.beautify_response()
#         assert self.html_tags[0] is None
#         return self.html_tags[0].findAll('img')

class ExtractLinks(BeautifulResponse):
    """
    This extracts all images from the html tags
    """
    @classmethod
    def get_links(cls, *args):
        self = cls
        cls.beautify_response(self)
        return cls.html_tags[0].findAll('a')

class ExtractImages(BeautifulResponse):
    """
    This extracts all images from the html tags
    """
    def get_images(self, *args):
        self.beautify_response()
        return self.html_tags[0].findAll('img')


