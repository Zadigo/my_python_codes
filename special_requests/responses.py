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
from useragent import UserAgentMixin

class BaseResponse(UserAgentMixin):
    urls = ['http://www.sawfirst.com']
    useragent = None
    
    def get_response(self, *args, **kwargs):
        if self.urls is None:
            raise ValueError('there')

        if type(self.urls).__name__ != 'list':
            raise TypeError('Received %s instead of a list' % type(self.urls).__name__)

        if len(self.urls) == 0:
            raise ValueError('There was no urls got %s' %  self.urls)

        if 'agent' in kwargs:
            self.useragent = kwargs.get('agent')
        else:
            self.useragent = self.get_rand_user_agent()
        
        try:
            # We send the requests to the server
            responses = [requests.get(url, self.useragent) for url in self.urls]

        except ConnectionError as error:
            print('There was an error. See %s with an adress' % (error.args))

        else:
            return responses
        return BaseResponse