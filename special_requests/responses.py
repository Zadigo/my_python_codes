"""
This module is used to create a GET request
to a given website and returns itself.

>>> class YourClass(BaseResponse):
>>>     urls = ['']
>>>     useragent = Your User Agent
"""
import requests
from bs4 import BeautifulSoup

class BaseResponse(object):
    urls = None
    useragent = None
    
    def get_response(self, *args, **kwargs):
        if self.urls is None:
            return None

        if type(self.urls).__name__ != 'list':
            raise TypeError('Received %s' % type(self.urls).__name__)

        if len(self.urls) == 0:
            raise TypeError('There was no urls got %s' %  self.urls)

        if 'agent' in kwargs:
            self.useragent = kwargs.get('agent')
        else:
            self.useragent = 'Mozilla 7.2 / Default'
        
        try:
            # We send the requests to the server
            responses = [requests.get(url, self.useragent) for url in self.urls]

        except ConnectionError as error:
            print('There was an error. See %s with an adress' % (error.args))

        else:
            return responses
        return BaseResponse