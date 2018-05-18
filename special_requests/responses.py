"""
This module is used to create a GET request
to a given website and returns itself.

The request is not executed until the user
is ready to do so.

>>> class YourClass(BaseResponse):
>>>     urls = ['']
>>>     useragent = Your User Agent
"""

import requests
from special_requests.useragent import UserAgentMixins

class BaseResponseMixins:
    url=''
    urls=[]
    def __init__(self):
        if not isinstance(self.urls, list):
            raise TypeError('URLs has to be a list. Got %s' % self.urls.__class__)

class BaseResponse(BaseResponseMixins, UserAgentMixins):
    def raw_response(self):
        try:
            if self.url:
                response    = [requests.get(self.url, self.get_rand_user_agent())]
            elif self.urls:
                response    = [requests.get(url, self.get_rand_user_agent()) for url in self.urls]
            else:
                raise requests.exceptions.MissingSchema('There were no urls.')

        except ConnectionError as error:
            print('There %s' % error.args)
        
        return [resp for resp in response if resp.status_code == 200]