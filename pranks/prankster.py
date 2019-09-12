from threading import Thread
import requests
from requests import Request, Session, options
import secrets

class Prankster:
    def __init__(self, url, data):
        self.data = self.prepare_data(data)

        session = Session()        
        request = Request(method='post', url=url, data=data)
        prepared_request = session.prepare_request(request)
        response = session.send(prepared_request)
        print('[%s]: %s' % (response.status_code, url))
            

    def prepare_headers(self, **kwargs):
        headers = {
            'User-Agent': secrets.token_hex(78),
            'DNT': 0
        }

        if kwargs:
            headers.update(**kwargs)
        return headers

    def prepare_data(self, data):
        data = {
            'email': 'email'
        }
        return data
