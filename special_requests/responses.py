import requests
from bs4 import BeautifulSoup

class BaseResponse(object):
    urls = None
    useragent = None

    def get_response(self, *args, **kwargs):
        if self.urls is None:
            return None
        # assert self.urls is not None

        if type(self.urls).__name__ != 'list':
            raise TypeError('Receive %s' % type(self.urls).__name__)
        # assert type(self.urls).__name__ != 'list'

        if len(self.urls) == 0:
            raise TypeError('There was no urls got %s' %  self.urls)
        # assert len(self.urls) == 0

        
        if 'agent' in kwargs:
            self.useragent = kwargs.get('agent')
        else:
            self.useragent = 'Mozilla 7.2 / Default'
        
        try:
            responses = [requests.get(url, self.useragent) for url in self.urls]

        except ConnectionError as error:
            print('There was an error. See %s with this adress' % (error.args, url))

        else:
            # return responses or None
            return responses
        return BaseResponse