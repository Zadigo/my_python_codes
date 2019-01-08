import time
import requests
from sr_settings import URLS
# from customuseragents import get_rand_user_agent

class BaseResponse:
    def __init__(self, method='GET', **kwargs):
        if not isinstance(URLS, (list, tuple)):
            raise TypeError('')

        if method == 'POST':
            if data in kwargs:
                data = kwargs['data']
            self.responses = [requests.post(url, data=data) for url in URLS]
        else:
            self.responses = [requests.get(url, "Mozilla/5.0 (Android 8.0; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0") for url in URLS]
    
    @property
    def _response_engine(self):
        response_klass = type('Responses', (), {
            'responses': self.responses,
            'responses_status_code': [response.status_code for response in self.responses],
            '__doc__': 'A class containing all the responses'
            }
        )
        return response_klass


class Responses(BaseResponse):
    @property
    def raw_responses(self):
        return self.responses

    def _curate(self):
        # Filter the responses leaving only
        # those with a 200 status
        curated_responses = [response for response in self.responses if response.status_code == 200]
        return curated_responses
